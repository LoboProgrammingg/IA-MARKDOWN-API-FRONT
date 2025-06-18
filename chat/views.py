# chat/views.py

import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatMessage # Garanta que o modelo foi importado

# O endereço do seu backend de IA
API_URL = 'http://127.0.0.1:8000/chat/multi'

def home_view(request):
    """
    Renderiza a página inicial do site.
    """
    return render(request, 'chat/home.html')

@login_required # Apenas usuários logados podem acessar
def chat_view(request):
    """
    Controla a lógica da página de chat.
    """
    # Busca o histórico de mensagens do usuário logado para exibir na página
    historico = ChatMessage.objects.filter(user=request.user).order_by('timestamp')
    
    context = {
        'historico': historico
    }

    # Se o usuário enviou o formulário (fez uma pergunta)
    if request.method == 'POST':
        pergunta_usuario = request.POST.get('pergunta', '')

        if pergunta_usuario:
            # Prepara os dados para enviar à API
            session_id = f'user_{request.user.id}'
            payload = {'pergunta': pergunta_usuario, 'session_id': session_id}

            try:
                # *** AQUI É ONDE ELE "PUXA DA API" ***
                response = requests.post(API_URL, json=payload, timeout=120)
                response.raise_for_status() 

                # Processa a resposta da API
                api_data = response.json()
                resposta_ia = api_data.get('resposta', 'Não foi possível obter uma resposta.')

                # Salva a conversa no banco de dados do Django
                ChatMessage.objects.create(
                    user=request.user,
                    pergunta=pergunta_usuario,
                    resposta=resposta_ia
                )
                
                # Redireciona para a mesma página para mostrar a nova mensagem no histórico
                return redirect('chat_page')

            except requests.exceptions.RequestException as e:
                # Se a API falhar, mostra um erro
                context['erro'] = f"Erro de comunicação com a IA: {e}"

    # Renderiza a página
    return render(request, 'chat/chat_page.html', context)