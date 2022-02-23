from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from categoria.models import Categoria
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from .models import Post
from django.db.models import Count, Case, When, Q
from django.contrib import messages


class PostIndex(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 6

    # adiciona outro objeto para consulta no template_name
    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)
        cd['categorias'] = Categoria.objects.all()

        return cd

    # get_queryset é um método da classes q estamos herdando, com ela vc faz edições no q quer exibir
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('categoria')
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

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        qs = qs.filter(
            Q(titulo__icontains=termo) |
            Q(autor__username__iexact=termo) |
            Q(conteudo__icontains=termo) |
            Q(categoria__nome_cat__iexact=termo) |
            Q(excerto__icontains=termo)

        )

        return qs


class PostCategoria(PostIndex):
    template_name = 'post_categoria.html'

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.kwargs.get('categoria', None)
        qs = qs.filter(categoria__nome_cat__iexact=categoria)

        return qs


class PostDetalhes(UpdateView):
    template_name = 'post_detalhe.html'
    model = Post
    form_class = FormComentario
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)
        post_atual = self.get_object()
        cd['comentarios'] = Comentario.objects.filter(publicado_comentario=True,
                                                      post_comentario=post_atual.id)

        return cd

    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post

        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user

        comentario.save()
        messages.success(self.request, 'Comentario enviado!')
        return redirect('post_detalhe', pk=post.id)
