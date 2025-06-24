from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.logout_request_view, name='logout'),

    path('', views.landing_page_view, name='landing_page'),

    path('post/<slug:slug>/', views.post_detail_view, name='post_detail'),

    path('chat/', views.chat_view, name='chat'),
    path('documentos/', views.document_list_view, name='document_list'),
    path('dashboards/', views.dashboard_view, name='dashboards'),
    path('perfil/', views.profile_view, name='profile'),
    
    path('api/chat/', views.chat_api_view, name='chat_api'),
    path('api/feedback/', views.feedback_api_view, name='feedback_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
