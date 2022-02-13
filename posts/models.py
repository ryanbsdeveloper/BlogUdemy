from pickle import TRUE
from categoria.models import Categoria
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(default=timezone.now)
    conteudo = models.TextField()
    excerto = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=None)
    imagem = models.ImageField(upload_to='fotos_dos_posts/%Y/%m', blank=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo