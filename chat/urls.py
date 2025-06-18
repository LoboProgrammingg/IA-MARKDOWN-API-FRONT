from django.urls import path
from .views import chat_view, profile_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    
    path('chat/', chat_view, name='chat_page'),
    path('perfil/', profile_view, name='profile'),
]