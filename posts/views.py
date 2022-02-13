from itertools import count
from re import template
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Count, Case, When


class PostIndex(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 6

    # get_queryset é um método da classes q estamos herdando, com ela vc faz edições no q quer exibir
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id')
        qs = qs.filter(publicado=True)
        # annotate criar um campo adicional no objeto para ser usado, fica junto com os
        # dados do banco de dados, mais ele não é adicionado na base de dados!
        # ai você faz as validações que desejar.
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )

        return qs


class PostBusca(PostIndex):
    template_name = 'post_busca.html'


class PostCategoria(PostIndex):
    template_name = 'post_categoria.html'


class PostDetalhes(UpdateView):
    pass
