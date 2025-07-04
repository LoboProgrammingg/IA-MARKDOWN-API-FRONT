import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_project.settings')
django.setup()

User = get_user_model()

username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'matheuscamara')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'sarutobi12')

if not User.objects.filter(username=username).exists():
    print(f"Criando superusuário '{username}'...")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print(f"Superusuário '{username}' já existe.")