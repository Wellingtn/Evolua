from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'ra', 'curso', 'semestre', 'professor', 'email', 'senha']
