# createsuper.py
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nome_do_seu_projeto.settings')
import django
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()
username = "matheuscamara"
email = "admin@example.com"
password = "sarutobi12"
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser criado!")
else:
    print("Superuser já existe.")