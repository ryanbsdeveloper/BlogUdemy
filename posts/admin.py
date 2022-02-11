from django.contrib import admin
from .models import Posts

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'autor', 'titulo', 'categoria', 'publicado')
    list_editable = ['publicado']
    list_display_links = ['id', 'autor']

admin.site.register(Posts, PostAdmin)