import json
import requests
import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.contrib import messages

from .models import Document, ChatMessage, Profile, Post
from .forms import UserUpdateForm, ProfileUpdateForm

API_LANGCHAIN_URL = 'http://127.0.0.1:8000/chat/multi'


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
                return JsonResponse(
                    {'error': 'Valor de feedback inválido.'}, status=400
                )

            message = ChatMessage.objects.get(id=message_id, user=request.user)
            message.feedback = feedback_value
            message.save()

            return JsonResponse(
                {
                    'success': True,
                    'message': 'Feedback registrado com sucesso.',
                }
            )
        except ChatMessage.DoesNotExist:
            return JsonResponse(
                {
                    'error': 'Mensagem não encontrada ou não pertence ao usuário.'
                },
                status=404,
            )
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método não permitido.'}, status=405)


@login_required
def chat_api_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    try:
        data = json.loads(request.body)
        user_message = data.get('message')
        session_id = data.get('session_id', str(request.user.id))
        if not user_message:
            return JsonResponse({'error': 'Mensagem faltando.'}, status=400)

        payload = {'pergunta': user_message, 'session_id': session_id}
        response = requests.post(API_LANGCHAIN_URL, data=payload)
        response.raise_for_status()

        api_response_data = response.json()
        bot_response = api_response_data.get(
            'resposta', 'Desculpe, não consegui obter uma resposta.'
        )

        chat_message = ChatMessage.objects.create(
            user=request.user, message=user_message, response=bot_response
        )

        return JsonResponse(
            {'response': bot_response, 'message_id': chat_message.id}
        )
    except Exception as e:
        return JsonResponse({'error': f'Erro: {e}'}, status=500)


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