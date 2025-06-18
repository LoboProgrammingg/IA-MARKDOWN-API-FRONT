import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import logout
from .models import ChatMessage
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

API_URL = 'http://127.0.0.1:8000/chat/multi'

def home_view(request):
    return render(request, 'chat/home.html', {'active_nav': 'home'})

@login_required
def chat_view(request):
    if request.method == 'GET':
        historico = ChatMessage.objects.filter(user=request.user).order_by('timestamp')
        context = {'historico': historico, 'active_nav': 'chat'}
        return render(request, 'chat/chat_page.html', context)

    if request.method == 'POST':
        print("\n--- [DJANGO] INICIANDO REQUISIÇÃO POST ---")
        pergunta_usuario = request.POST.get('pergunta', '')

        if not pergunta_usuario:
            print("[DJANGO] ERRO: Pergunta vazia.")
            return JsonResponse({'erro': 'A pergunta não pode estar vazia.'}, status=400)

        session_id = f'user_{request.user.id}'
        payload = {'pergunta': pergunta_usuario, 'session_id': session_id}
        print(f"1. [DJANGO] Payload para a API pronto: {payload}")

        try:
            print("2. [DJANGO] Enviando requisição para a API FastAPI...")
            response = requests.post(API_URL, data=payload, timeout=120)
            print(f"3. [DJANGO] Resposta da API recebida com status: {response.status_code}")
            response.raise_for_status()

            api_data = response.json()
            resposta_ia = api_data.get('resposta', 'ERRO: Chave "resposta" não encontrada no JSON da API.')
            print(f"4. [DJANGO] Resposta da IA extraída: {resposta_ia[:70]}...")

            ChatMessage.objects.create(
                user=request.user,
                pergunta=pergunta_usuario,
                resposta=resposta_ia
            )
            print("5. [DJANGO] Mensagem salva no banco de dados.")
            
            print("6. [DJANGO] Retornando JsonResponse para o JavaScript.")
            return JsonResponse({'pergunta': pergunta_usuario, 'resposta': resposta_ia})

        except requests.exceptions.RequestException as e:
            print(f"!!! [DJANGO] ERRO DE CONEXÃO COM A API: {e}")
            return JsonResponse({'erro': f'Erro de comunicação com a IA: {e}'}, status=500)
        except Exception as e:
            # Pega qualquer outro erro que possa acontecer (ex: falha ao salvar no DB)
            print(f"!!! [DJANGO] ERRO INESPERADO NA VIEW: {e}")
            return JsonResponse({'erro': f'Um erro inesperado ocorreu no servidor Django: {e}'}, status=500)
        
@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'chat/profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')