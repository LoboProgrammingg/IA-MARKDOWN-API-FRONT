# chat/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pergunta = models.TextField()
    resposta = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.pergunta[:30]}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unidade = models.CharField(max_length=100, blank=True, null=True, verbose_name="Unidade/Setor")
    foto = models.ImageField(upload_to='avatars/', default='avatars/default.png', verbose_name="Foto de Perfil")

    def __str__(self):
        return f'Perfil de {self.user.username}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)