from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    ra = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    semestre = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # Será armazenada de forma segura.

    def __str__(self):
        return f"{self.nome} {self.sobrenome} ({self.ra})"

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # Será armazenada de forma segura.

    def __str__(self):
        return f"{self.nome} ({self.email})"

class Turma(models.Model):
    id_turma = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='turmas')
    alunos = models.ManyToManyField(Aluno)

    def __str__(self):
        return f"Turma {self.id_turma} - Prof. {self.professor.nome}"

class Resposta(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    resposta_1 = models.BooleanField(default=None, null=True)
    resposta_2 = models.BooleanField(default=None, null=True)
    resposta_3 = models.BooleanField(default=None, null=True)
    resposta_4 = models.TextField(blank=True, null=True)
    resposta_5 = models.BooleanField(default=None, null=True)
    resposta_6 = models.BooleanField(default=None, null=True)
    resposta_7 = models.BooleanField(default=None, null=True)
    resposta_8 = models.BooleanField(default=None, null=True)
    resposta_9 = models.TextField(blank=True, null=True)
    resposta_10 = models.BooleanField(default=None, null=True)
    resposta_11 = models.TextField(blank=True, null=True)
    resposta_12 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Respostas de {self.aluno.nome} {self.aluno.sobrenome}"
