# core/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Importa todos os modelos, incluindo o novo DashboardData
from .models import Document, ChatMessage, Profile, DashboardData

# ===================================================================
# ADMIN PARA O MODELO DOCUMENT
# ===================================================================
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'uploaded_at')
    search_fields = ('title', 'description')
    list_filter = ('uploaded_at',)
    date_hierarchy = 'uploaded_at'
    ordering = ['-uploaded_at']

    @admin.display(description="Pré-visualização da Capa")
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 80px; max-width: 100px;" />')
        return "Sem Imagem"

# ===================================================================
# ADMIN PARA O MODELO CHATMESSAGE
# ===================================================================
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    # Adicionamos 'feedback' para ver o status diretamente na lista
    list_display = ('user', 'message', 'created_at', 'get_feedback_display')
    list_filter = ('created_at', 'user', 'feedback') # Adicionado filtro por feedback
    search_fields = ('message', 'response', 'user__username')
    
    # Adicionamos 'feedback' aos campos de leitura
    readonly_fields = ('user', 'message', 'response', 'created_at', 'feedback')

    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
        
    # Esta função busca o nome legível do 'choice' que definimos no modelo
    @admin.display(description="Feedback")
    def get_feedback_display(self, obj):
        return obj.get_feedback_display()

# ===================================================================
# ADMIN PARA O NOVO MODELO DashboardData
# ===================================================================
@admin.register(DashboardData)
class DashboardDataAdmin(admin.ModelAdmin):
    """
    Configuração para gerenciar os arquivos de dados para os dashboards.
    """
    list_display = ('title', 'unidade', 'uploaded_at')
    list_filter = ('unidade', 'uploaded_at')
    search_fields = ('title', 'unidade')
    ordering = ['-uploaded_at']

# ===================================================================
# ADMIN CUSTOMIZADO PARA USER E PROFILE
# ===================================================================
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfil do Usuário'
    fk_name = 'user'

class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
