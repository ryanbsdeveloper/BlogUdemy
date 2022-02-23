from django.forms import ModelForm
from .models import Comentario


class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')

        if len(nome) < 4:
            self.add_error('nome_comentario','Nome muito curto!')
            
    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')