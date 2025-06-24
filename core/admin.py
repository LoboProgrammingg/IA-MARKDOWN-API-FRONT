from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from .utils import generate_ai_image, generate_prompt_from_content

from .models import Document, ChatMessage, Profile, Post

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

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'get_feedback_display')
    list_filter = ('created_at', 'user', 'feedback')
    search_fields = ('message', 'response', 'user__username')
    readonly_fields = ('user', 'message', 'response', 'created_at', 'feedback')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
        
    @admin.display(description="Feedback")
    def get_feedback_display(self, obj):
        return obj.get_feedback_display()

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_type', 'status', 'created_at')
    list_filter = ('status', 'post_type', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    ordering = ('status', '-created_at')

    # Organiza os campos no painel de admin para uma melhor UX
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'status', 'post_type', 'author')
        }),
        ('Conteúdo Principal', {
            'classes': ('collapse',),
            'fields': ('content',),
        }),
        ('Imagem de Destaque (Gerada por IA se vazia)', {
            'fields': ('featured_image', 'short_description', 'image_prompt'),
            'description': "Se nenhuma imagem for enviada, uma será gerada pela IA com base na 'Descrição Curta' ou, se vazia, no 'Prompt Customizado'. Se ambos estiverem vazios, um prompt será gerado a partir do conteúdo."
        }),
    )

    def save_model(self, request, obj, form, change):
        # Define o autor automaticamente se for uma nova postagem
        if not obj.author_id:
            obj.author = request.user

        # Lógica de Geração de Imagem por IA
        if not obj.featured_image:
            # Define a hierarquia de prompts: customizado > descrição > conteúdo
            prompt = obj.image_prompt or obj.short_description or generate_prompt_from_content(obj.content)
            
            if prompt:
                ai_image_file = generate_ai_image(prompt)
                if ai_image_file:
                    # Salva o arquivo no campo de imagem, mas não salva o modelo ainda
                    obj.featured_image.save(ai_image_file.name, ai_image_file, save=False)

        # Salva o objeto Post no banco de dados com todas as alterações
        super().save_model(request, obj, form, change)

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
