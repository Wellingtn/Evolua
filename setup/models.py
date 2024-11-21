from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    ra = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    semestre = models.PositiveIntegerField()
    professor = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # Será armazenada de forma segura.

    def __str__(self):
        return f"{self.nome} {self.sobrenome} ({self.ra})"
