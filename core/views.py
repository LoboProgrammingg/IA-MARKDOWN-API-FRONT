import json
import requests
import uuid
import logging   # Importa o módulo de logging

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.contrib import messages

from .models import Document, ChatMessage, Profile, Post
from .forms import UserUpdateForm, ProfileUpdateForm

logger = logging.getLogger(__name__)

API_LANGCHAIN_URL = 'http://127.0.0.1:8001/chat/multi'
API_TIMEOUT_SECONDS = 400


def landing_page_view(request):
    if request.user.is_authenticated:
        return redirect('chat')

    latest_posts = Post.objects.filter(status='PUBLISHED').order_by(
        '-created_at'
    )[:6]

    context = {
        'latest_posts': latest_posts,
    }
    return render(request, 'core/landing_page.html', context)


def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug, status='PUBLISHED')
    related_posts = (
        Post.objects.filter(status='PUBLISHED')
        .exclude(id=post.id)
        .order_by('-created_at')[:3]
    )

    context = {'post': post, 'related_posts': related_posts}
    return render(request, 'core/post_detail.html', context)


@login_required
def chat_view(request):
    chat_messages = ChatMessage.objects.filter(user=request.user).order_by(
        'created_at'
    )
    if 'chat_session_id' not in request.session:
        request.session['chat_session_id'] = str(uuid.uuid4())

    context = {
        'chat_session_id': request.session['chat_session_id'],
        'chat_messages': chat_messages,
    }
    return render(request, 'core/home.html', context)


@login_required
def dashboard_view(request):
    total_documents = Document.objects.count()
    likes = ChatMessage.objects.filter(feedback=1).count()
    dislikes = ChatMessage.objects.filter(feedback=-1).count()
    total_feedback = likes + dislikes
    like_percentage = (
        (likes / total_feedback * 100) if total_feedback > 0 else 0
    )

    top_users = (
        ChatMessage.objects.values('user__username', 'user__profile__image')
        .annotate(message_count=Count('id'))
        .order_by('-message_count')[:5]
    )

    recent_feedbacks = (
        ChatMessage.objects.exclude(feedback=0)
        .select_related('user')
        .order_by('-created_at')[:3]
    )
    recent_documents = Document.objects.order_by('-uploaded_at')[:3]

    context = {
        'total_documents': total_documents,
        'likes': likes,
        'dislikes': dislikes,
        'like_percentage': round(like_percentage, 1),
        'top_users': list(top_users),
        'recent_feedbacks': recent_feedbacks,
        'recent_documents': recent_documents,
    }
    return render(request, 'core/dashboards.html', context)


@login_required
def feedback_api_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message_id = data.get('message_id')
            feedback_value = data.get('feedback')

            if feedback_value not in [1, -1]:
                logger.warning(
                    f'Feedback inválido recebido de {request.user.username}: {feedback_value}'
                )
                return JsonResponse(
                    {'error': 'Valor de feedback inválido.'}, status=400
                )

            message = get_object_or_404(
                ChatMessage, id=message_id, user=request.user
            )
            message.feedback = feedback_value
            message.save()
            logger.info(
                f'Feedback registrado para mensagem {message_id} por {request.user.username}: {feedback_value}'
            )

            return JsonResponse(
                {
                    'success': True,
                    'message': 'Feedback registrado com sucesso.',
                }
            )
        except json.JSONDecodeError:
            logger.error(
                f'Erro de decodificação JSON no feedback de {request.user.username}'
            )
            return JsonResponse(
                {
                    'error': 'Requisição inválida. O corpo da requisição deve ser um JSON válido.'
                },
                status=400,
            )
        except ChatMessage.DoesNotExist:
            logger.warning(
                f'Mensagem {message_id} não encontrada ou não pertence ao usuário {request.user.username}.'
            )
            return JsonResponse(
                {
                    'error': 'Mensagem não encontrada ou não pertence ao usuário.'
                },
                status=404,
            )
        except Exception as e:
            logger.exception(
                f'Erro inesperado no feedback_api_view para o usuário {request.user.username}: {e}'
            )
            return JsonResponse(
                {'error': f'Erro interno do servidor: {str(e)}'}, status=500
            )

    logger.warning(
        f'Método não permitido para feedback_api_view: {request.method}'
    )
    return JsonResponse({'error': 'Método não permitido.'}, status=405)


@login_required
@csrf_exempt
def chat_api_view(request):
    if request.method != 'POST':
        logger.warning(
            f'Método não permitido para chat_api_view: {request.method}'
        )
        return JsonResponse({'error': 'Método não permitido'}, status=405)

    try:
        data = json.loads(request.body)

        user_message = data.get('pergunta') or data.get('message')

        session_id = data.get('session_id', str(request.user.id))

        if not user_message:
            logger.warning(
                f"Chave 'pergunta' ou 'message' faltando na requisição para o usuário {request.user.username}"
            )
            return JsonResponse(
                {'error': "Chave 'pergunta' ou 'message' faltando."},
                status=400,
            )

        payload = {'pergunta': user_message, 'session_id': session_id}

        logger.info(
            f'Usuário {request.user.username} enviou mensagem. Session ID: {session_id}'
        )
        logger.debug(f'Payload enviado para Langchain API: {payload}')

        response = requests.post(
            API_LANGCHAIN_URL, data=payload, timeout=API_TIMEOUT_SECONDS
        )

        response.raise_for_status()

        api_response_data = response.json()
        bot_response = api_response_data.get(
            'resposta', 'Desculpe, não consegui obter uma resposta da IA.'
        )

        logger.info(
            f'Resposta recebida da Langchain API para {request.user.username}. Comprimento da resposta: {len(bot_response)}'
        )

        chat_message = ChatMessage.objects.create(
            user=request.user, message=user_message, response=bot_response
        )
        logger.info(
            f'Mensagem de chat salva (ID: {chat_message.id}) para {request.user.username}.'
        )

        return JsonResponse(
            {'response': bot_response, 'message_id': chat_message.id}
        )

    except requests.exceptions.Timeout as e:
        logger.error(
            f'Erro de Timeout da Langchain API para o usuário {request.user.username} após {API_TIMEOUT_SECONDS} segundos: {e}'
        )
        return JsonResponse(
            {
                'error': 'O servidor de IA demorou muito para responder. Por favor, tente novamente mais tarde.',
                'code': 'API_TIMEOUT',
            },
            status=504,
        )
    except requests.exceptions.ConnectionError as e:
        logger.error(
            f'Erro de Conexão com a Langchain API para o usuário {request.user.username}: {e}'
        )
        return JsonResponse(
            {
                'error': 'Não foi possível conectar ao servidor de IA. Verifique se ele está ativo e acessível.',
                'code': 'API_CONNECTION_ERROR',
            },
            status=503,
        )
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        error_detail = e.response.text
        logger.error(
            f'Erro HTTP da Langchain API ({status_code}) para o usuário {request.user.username}: {error_detail}'
        )
        return JsonResponse(
            {
                'error': f'A API de IA retornou um erro: {status_code}. Detalhes: {error_detail}',
                'code': 'API_HTTP_ERROR',
            },
            status=status_code,
        )
    except json.JSONDecodeError as e:
        logger.error(
            f'Erro de decodificação JSON para o usuário {request.user.username}: {e}'
        )
        return JsonResponse(
            {
                'error': 'Formato de dados inválido na requisição.',
                'code': 'JSON_PARSE_ERROR',
            },
            status=400,
        )
    except Exception as e:
        logger.exception(
            f'Erro inesperado no chat_api_view para o usuário {request.user.username}: {e}'
        )
        return JsonResponse(
            {
                'error': f'Erro interno do servidor: {str(e)}. Por favor, tente novamente ou contate o suporte.',
                'code': 'UNEXPECTED_ERROR',
            },
            status=500,
        )


@login_required
def document_list_view(request):
    search_query = request.GET.get('q', '')
    document_list = Document.objects.all().order_by('-uploaded_at')
    if search_query:
        document_list = document_list.filter(
            Q(title__icontains=search_query)
            | Q(description__icontains=search_query)
        )

    paginator = Paginator(document_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'search_query': search_query}
    return render(request, 'core/document_list.html', context)


@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Perfil Atualizado com SUCESSO!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'core/profile.html', context)


def logout_request_view(request):
    logout(request)
    return redirect('landing_page')
