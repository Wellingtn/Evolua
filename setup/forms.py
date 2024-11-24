from django import forms
from .models import Aluno, Resposta, Professor, Turma


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

class TurmaForm(forms.ModelForm):
    alunos = forms.ModelMultipleChoiceField(
        queryset=Aluno.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Turma
        fields = ['nome', 'alunos']

    def __init__(self, *args, **kwargs):
            self.professor = kwargs.pop('professor', None)
            super(TurmaForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        turma = super(TurmaForm, self).save(commit=False)
        turma.professor = self.professor
        if commit:
            turma.save()
            self.save_m2m()
        return turma