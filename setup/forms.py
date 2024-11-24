from django import forms
from .models import Aluno, Resposta, Professor


class AlunoForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'ra', 'curso', 'semestre', 'email', 'senha']

class ProfessorForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Professor
        fields = ['nome', 'email', 'senha']

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = [f'resposta_{i}' for i in range(1, 13)]
        widgets = {
            'resposta_1': forms.RadioSelect(choices=[(True, 'Sim'), (False, 'Não')]),
            'resposta_2': forms.RadioSelect(choices=[(True, 'Sim'), (False, 'Não')]),
            'resposta_3': forms.RadioSelect(choices=[(True, 'Sim'), (False, 'Não')]),
            'resposta_4': forms.Textarea(attrs={'rows': 3}),
            'resposta_5': forms.RadioSelect(choices=[(True, 'Sim'), (False, 'Não')]),
            'resposta_6': forms.RadioSelect(choices=[(True, 'Sim'), (False, 'Não')]),
            'resposta_7': forms.RadioSelect(choices=[(True, 'Sim'), (False, 'Não')]),
            'resposta_8': forms.RadioSelect(choices=[(True, 'Sim'), (False, 'Não')]),
            'resposta_9': forms.Textarea(attrs={'rows': 3}),
            'resposta_10': forms.RadioSelect(choices=[(True, 'Sim'), (False, 'Não')]),
            'resposta_11': forms.Textarea(attrs={'rows': 3}),
            'resposta_12': forms.Textarea(attrs={'rows': 3}),
        }