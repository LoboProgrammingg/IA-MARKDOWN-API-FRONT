# create_render_superuser.py
import os
import django
from django.conf import settings
from django.contrib.auth import get_user_model

# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_project.settings') # ATENÇÃO: SUBSTITUA 'site_project' PELO NOME DA SUA PASTA PRINCIPAL DO DJANGO
django.setup()

User = get_user_model()

if settings.RENDER_CREATE_SUPERUSER:
    username = settings.RENDER_SUPERUSER_USERNAME
    email = settings.RENDER_SUPERUSER_EMAIL
    password = settings.RENDER_SUPERUSER_PASSWORD

    if not (username and email and password):
        print("ERRO: Variáveis de ambiente para superuser não definidas. Não foi possível criar o superuser.")
    elif User.objects.filter(username=username).exists():
        print(f"Superuser '{username}' já existe. Ignorando criação.")
    else:
        try:
            print(f"Tentando criar superuser '{username}'...")
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superuser '{username}' criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar superuser '{username}': {e}")
else:
    print("Criação de superuser via Render desabilitada.")