# core/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# O modelo Document permanece o mesmo.
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

# O modelo Profile permanece o mesmo.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    unidade = models.CharField(max_length=100, blank=True, null=True, verbose_name="Unidade/Setor")
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics', verbose_name="Foto de Perfil")

    def __str__(self):
        return f'Perfil de {self.user.username}'

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

# Os sinais para o Profile permanecem os mesmos.
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# O modelo ChatMessage com o novo campo de feedback
class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    message = models.TextField(verbose_name="Mensagem do Usuário")
    response = models.TextField(verbose_name="Resposta do Bot")
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ===============================================================
    # NOVO CAMPO ADICIONADO
    # ===============================================================
    # 1 para 'Gostei', -1 para 'Não Gostei', 0 para sem feedback.
    feedback = models.IntegerField(default=0, choices=[(1, 'Gostei'), (-1, 'Não Gostei'), (0, 'Nenhum')])

    def __str__(self):
        return f"Mensagem de {self.user.username} em {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Mensagem do Chat"
        verbose_name_plural = "Mensagens do Chat"
        ordering = ['-created_at']

# O modelo DashboardData é removido, pois não usaremos mais CSVs para este dashboard.
# Se você o usa para outra coisa, pode mantê-lo. Caso contrário, pode ser deletado.
class DashboardData(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título do Conjunto de Dados")
    unidade = models.CharField(max_length=100, verbose_name="Unidade Correspondente", help_text="A qual unidade/setor estes dados pertencem.")
    csv_file = models.FileField(upload_to='dashboards/csvs/', verbose_name="Arquivo CSV")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Upload")

    def __str__(self):
        return f'{self.title} ({self.unidade})'

    class Meta:
        verbose_name = "Dado para Dashboard"
        verbose_name_plural = "Dados para Dashboards"
        ordering = ['-uploaded_at']
