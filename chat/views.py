# chat/views.py

import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatMessage

API_URL = 'http://127.0.0.1:8000/chat/multi'

def home_view(request):

    return render(request, 'chat/home.html')

@login_required
def chat_view(request):

    historico = ChatMessage.objects.filter(user=request.user).order_by('timestamp')
    
    context = {
        'historico': historico
    }

    if request.method == 'POST':
        pergunta_usuario = request.POST.get('pergunta', '')

        if pergunta_usuario:
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
                
                return redirect('chat_page')

            except requests.exceptions.RequestException as e:
                context['erro'] = f"Não foi possível conectar à IA. Tente novamente mais tarde. (Erro: {e})"

    return render(request, 'chat/chat_page.html', context)