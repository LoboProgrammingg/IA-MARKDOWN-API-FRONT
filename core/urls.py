# core/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # URLs de Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.logout_request_view, name='logout'),

    # URLs da Aplicação
    path('', views.home_view, name='home'),
    path('api/chat/', views.chat_api_view, name='chat_api'),
    path('documentos/', views.document_list_view, name='document_list'),
    path('dashboards/', views.dashboard_view, name='dashboards'),
    path('perfil/', views.profile_view, name='profile'),
    
    path('api/feedback/', views.feedback_api_view, name='feedback_api'),
]

if settings.DEBUG: # <--
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)