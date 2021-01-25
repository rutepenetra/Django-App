from django import forms
from .models import Jogador


class JogadorForm(forms.ModelForm):

    class Meta:
        model = Jogador
        fields = ('nome','data_nasc','nif','telefone', 'email', 'morada')
        labels = {
            'nome':'Nome Completo',
            'data_nasc':'Data Nascimento',
            'nif':'Nº de Contribuinte',
            'telefone':'Telefone',
            'email':'Email',
            'morada':'Morada'
        }

