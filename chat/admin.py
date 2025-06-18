# chat/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile, ChatMessage


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfil do Usuário'
    fk_name = 'user'

class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_select_related = ('profile',)

    def get_unidade(self, instance):
        return instance.profile.unidade
    get_unidade.short_description = 'Unidade'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):

    list_display = ('user', 'pergunta_truncada', 'timestamp')
    
    list_filter = ('user', 'timestamp')
    
    search_fields = ('pergunta', 'resposta')
    
    ordering = ('-timestamp',)

    readonly_fields = ('user', 'pergunta', 'resposta', 'timestamp')

    def pergunta_truncada(self, obj):
        return obj.pergunta[:50] + '...' if len(obj.pergunta) > 50 else obj.pergunta
    pergunta_truncada.short_description = 'Pergunta'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'unidade')