import site
from django.contrib import admin
from .models import Categoria

class CatAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_cat']

admin.site.register(Categoria, CatAdmin)
