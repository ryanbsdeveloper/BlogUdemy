from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=100, verbose_name='Nome')
    email_comentario = models.EmailField(blank=True, verbose_name='E-mail')
    comentario = models.TextField(verbose_name='Comentario')
    post_comentario = models.ForeignKey(Post, models.CASCADE, verbose_name='Post') 
    usuario_comentario = models.ForeignKey(User, models.DO_NOTHING, verbose_name='Usuário', blank=True, null=None)
    data_comentario = models.DateTimeField(default=timezone.now, verbose_name='Data de publicação')
    publicado_comentario = models.BooleanField(default=True, verbose_name='Publicado')

    def __str__(self):
        return self.nome_comentario