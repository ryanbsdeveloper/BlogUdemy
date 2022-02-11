from django.contrib import admin
from .models import Comentario

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ['id', 'email_comentario', 'post_comentario',
                    'usuario_comentario', 'data_comentario', 'publicado_comentario']
    list_editable = ['publicado_comentario']
    list_display_links = ['id', 'email_comentario', 'post_comentario',
                          'usuario_comentario']

admin.site.register(Comentario, ComentariosAdmin)