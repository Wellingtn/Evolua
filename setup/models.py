from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    ra = models.CharField(max_length=6, unique=True)
    semestre = models.PositiveIntegerField(choices=[
        (1, "1° semestre"),
        (2, "2° semestre"),
        (3, "3° semestre"),
        (4, "4° semestre"),
        (5, "5° semestre"),
        (6, "6° semestre"),
        (7, "7° semestre"),
        (8, "8° semestre"),
    ])
    curso = models.CharField(max_length=50, choices=[
        ("Sistemas de Informação", "Sistemas de Informação"),
        ("Direito", "Direito"),
        ("Ontopsicologia", "Ontopsicologia"),
        ("Administração", "Administração"),
        ("Ciências Contábeis", "Ciências Contábeis"),
        ("Hotelaria", "Hotelaria"),
        ("Gastronomia", "Gastronomia"),
        ("Pedagogia", "Pedagogia"),
    ])
    professor = models.CharField(max_length=50, choices=[
        ("Gustavo Florêncio", "Gustavo Florêncio"),
        ("Patrícia Wazlawick", "Patrícia Wazlawick"),
        ("Gustavo Bernadini", "Gustavo Bernadini"),
        ("Jocássio Guidetti", "Jocássio Guidetti"),
    ])
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  

    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.ra}"