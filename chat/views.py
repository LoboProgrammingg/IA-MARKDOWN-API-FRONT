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
        pergunta_usuario = request.POST.get('pergunta', '')

        if not pergunta_usuario:
            return JsonResponse({'erro': 'A pergunta não pode estar vazia.'}, status=400)

        session_id = f'user_{request.user.id}'
        payload = {'pergunta': pergunta_usuario, 'session_id': session_id}

        try:
            response = requests.post(API_URL, json=payload, timeout=120)
            response.raise_for_status()

            api_data = response.json()
            resposta_ia = api_data.get('resposta', 'Não foi possível obter uma resposta.')

            ChatMessage.objects.create(
                user=request.user,
                pergunta=pergunta_usuario,
                resposta=resposta_ia
            )
            
            return JsonResponse({'pergunta': pergunta_usuario, 'resposta': resposta_ia})

        except requests.exceptions.RequestException as e:
            return JsonResponse({'erro': f'Erro de comunicação com a IA: {e}'}, status=500)
        
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