from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'autor', 'titulo', 'categoria', 'data', 'publicado')
    list_editable = ['publicado']
    list_display_links = ['id', 'autor', 'titulo', 'categoria', ]
    summernote_fields = 'conteudo'



admin.site.register(Post, PostAdmin)
