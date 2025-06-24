from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

class Document(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    file = models.FileField(upload_to='documents/files/', verbose_name="Arquivo PDF")
    image = models.ImageField(
        upload_to='documents/thumbnails/', 
        verbose_name="Imagem de Capa",
        blank=True, 
        null=True,
        help_text="Imagem de capa que será exibida no card do documento."
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Upload")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        ordering = ['-uploaded_at']

class Profile(models.Model):
    class UnidadeChoices(models.TextChoices):
        ASSCOM = 'ASSCOM', 'ASSCOM'
        DAFI = 'DAFI', 'DAFI'
        DIRC = 'DIRC', 'DIRC'
        DTIC = 'DTIC', 'DTIC'
        GABD = 'GABD', 'GABD'
        GACD = 'GACD', 'GACD'
        GADP = 'GADP', 'GADP'
        GAOI = 'GAOI', 'GAOI'
        GAQS = 'GAQS', 'GAQS'
        GASI = 'GASI', 'GASI'
        GCCP = 'GCCP', 'GCCP'
        GCES = 'GCES', 'GCES'
        GCOT = 'GCOT', 'GCOT'
        GCTO = 'GCTO', 'GCTO'
        GEDC = 'GEDC', 'GEDC'
        GEFI = 'GEFI', 'GEFI'
        GEGD = 'GEGD', 'GEGD'
        GEOR = 'GEOR', 'GEOR'
        GEPM = 'GEPM', 'GEPM'
        GEPP = 'GEPP', 'GEPP'
        GGES = 'GGES', 'GGES'
        GETS = 'GETS', 'GETS'
        GFAC = 'GFAC', 'GFAC'
        GFTG = 'GFTG', 'GFTG'
        GICF = 'GICF', 'GICF'
        GIAP = 'GIAP', 'GIAP'
        GPAC = 'GPAC', 'GPAC'
        GPGD = 'GPGD', 'GPGD'
        GPIN = 'GPIN', 'GPIN'
        GPMM = 'GPMM', 'GPMM'
        GPSE = 'GPSE', 'GPSE'
        GSPT = 'GSPT', 'GSPT'
        GRCO = 'GRCO', 'GRCO'
        GSIC = 'GSIC', 'GSIC'
        GSUP = 'GSUP', 'GSUP'
        OUVIDORIA = 'OUVIDORIA', 'OUVIDORIA'
        UGADM = 'UGADM', 'UGADM'
        UGACO = 'UGACO', 'UGACO'
        UGARQ = 'UGARQ', 'UGARQ'
        UGCOF = 'UGCOF', 'UGCOF'
        UGGDC = 'UGGDC', 'UGGDC'
        UGGDI = 'UGGDI', 'UGGDI'
        UGGOV = 'UGGOV', 'UGGOV'
        UGITI = 'UGITI', 'UGITI'
        UGPES = 'UGPES', 'UGPES'
        UGPRO = 'UGPRO', 'UGPRO'
        UGSDG = 'UGSDG', 'UGSDG'
        UGSTI = 'UGSTI', 'UGSTI'
        UGVEN = 'UGVEN', 'UGVEN'
        UGEPV = 'UGEPV', 'UGEPV'
        UGENP = 'UGENP', 'UGENP'
        UNICRS = 'UNICRS', 'UNICRS'
        UNIJUR = 'UNIJUR', 'UNIJUR'
        UNISECI = 'UNISECI', 'UNISECI'
        OUTRO = 'OUTRO', 'Outro / Não especificado'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    unidade = models.CharField(
        max_length=10, 
        choices=UnidadeChoices.choices, 
        blank=True, 
        null=True, 
        verbose_name="Unidade/Setor"
    )
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics', verbose_name="Foto de Perfil")

    def __str__(self):
        return f'Perfil de {self.user.username}'

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    message = models.TextField(verbose_name="Mensagem do Usuário")
    response = models.TextField(verbose_name="Resposta do Bot")
    created_at = models.DateTimeField(auto_now_add=True)
    feedback = models.IntegerField(default=0, choices=[(1, 'Gostei'), (-1, 'Não Gostei'), (0, 'Nenhum')])

    def __str__(self):
        return f"Mensagem de {self.user.username} em {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Mensagem do Chat"
        verbose_name_plural = "Mensagens do Chat"
        ordering = ['-created_at']

class Post(models.Model):
    class PostType(models.TextChoices):
        NEWS = 'NEWS', 'Notícia'
        ARTICLE = 'ARTICLE', 'Artigo'
        INSTRUCTION = 'INSTRUCTION', 'Instrução'
    class PostStatus(models.TextChoices):
        DRAFT = 'DRAFT', 'Rascunho'
        PUBLISHED = 'PUBLISHED', 'Publicado'

    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(max_length=220, unique=True, blank=True, help_text="Gerado automaticamente a partir do título.")
    content = models.TextField(verbose_name="Conteúdo")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='blog_posts', verbose_name="Autor")
    post_type = models.CharField(max_length=20, choices=PostType.choices, default=PostType.ARTICLE, verbose_name="Tipo de Postagem")
    status = models.CharField(max_length=10, choices=PostStatus.choices, default=PostStatus.DRAFT, verbose_name="Status")
    
    featured_image = models.ImageField(upload_to='posts/images/', verbose_name="Imagem de Destaque", blank=True, null=True, help_text="Faça o upload de uma imagem ou deixe em branco para a IA gerar uma.")
    short_description = models.CharField(max_length=255, blank=True, verbose_name="Descrição Curta (para IA)", help_text="Um resumo conciso para guiar a geração da imagem pela IA.")
    image_prompt = models.CharField(max_length=255, blank=True, verbose_name="Prompt Customizado (Opcional)", help_text="Instrução detalhada para a IA. Ex: 'Um cérebro de neon conectado a uma nuvem de dados'.")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"
        ordering = ['-created_at']
