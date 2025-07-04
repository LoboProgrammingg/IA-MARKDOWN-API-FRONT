import os
from pathlib import Path
import dj_database_url
from django.contrib.auth import get_user_model


API_IA_URL = os.environ.get("API_IA_URL", "https://api-ia-4lec.onrender.com/chat/multi")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-fallback-key-for-development-only')

DEBUG = os.environ.get('DEBUG_VALUE', 'False') == 'True'

ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME'), 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'site_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'site_project.wsgi.application'

# A SEÇÃO DO BANCO DE DADOS FOI ALTERADA AQUI
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',  # Fallback para desenvolvimento local
        conn_max_age=600  # Tempo de conexão máxima (em segundos)
    )
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Cuiaba'

USE_I18N = True

USE_TZ = True

JAZZMIN_SETTINGS = {
    'site_title': 'MTI',
    'site_header': 'MTI',
    'site_brand': 'MTI',
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
        'core.ChatMessage': 'fas fa-object-group',
        'core.Document': 'fas fa-copyright',
        'core.Post': 'fas fa-box',
    },
    'welcome_sign': 'Bem-vindo(a) ao Assistente da MTI',
    'copyright': 'UGGOV LTDA',
    'show_ui_builder': True,
}

JAZZMIN_UI_TWEAKS = {
    'navbar_small_text': False,
    'footer_small_text': False,
    'body_small_text': False,
    'brand_small_text': False,
    'brand_colour': 'navbar-primary',
    'accent': 'accent-primary',
    'navbar': 'navbar-white navbar-light',
    'no_navbar_border': False,
    'navbar_fixed': False,
    'layout_boxed': False,
    'footer_fixed': False,
    'sidebar_fixed': False,
    'sidebar': 'sidebar-light-primary',
    'sidebar_nav_small_text': False,
    'sidebar_disable_expand': False,
    'sidebar_nav_child_indent': False,
    'sidebar_nav_compact_style': False,
    'sidebar_nav_legacy_style': False,
    'sidebar_nav_flat_style': True,
    'theme': 'sandstone',
    'dark_mode_theme': None,
    'button_classes': {
        'primary': 'btn-outline-primary',
        'secondary': 'btn-outline-secondary',
        'info': 'btn-info',
        'warning': 'btn-warning',
        'danger': 'btn-danger',
        'success': 'btn-success',
    },
    'actions_sticky_top': False,
}

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [BASE_DIR / 'static']

WHITENOISE_KEEP_ONLY_HASHED_FILES = True
WHITENOISE_MAX_AGE = 31536000

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'chat'
LOGOUT_REDIRECT_URL = 'landing_page'