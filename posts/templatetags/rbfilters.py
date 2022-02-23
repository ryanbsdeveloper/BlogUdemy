from django import template

#essa variavel tem que ser register, não pode ter outro nome!
register = template.Library()


@register.filter(name='plural')
def plural(num):
    if num == 0:
        return 'Nenhum comentario'
    elif num == 1:
        return f'{num} Comentario'
    else:
        return f'{num} Comentarios' 
