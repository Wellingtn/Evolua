from django.urls import path
from . import views

app_name = 'setup'
urlpatterns = [
    path('', views.seleciona_usuario, name='index'),
    path('login/aluno/', views.login, name='login'),
    path('login/professor/', views.login_professor, name='login_professor'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro_professor/', views.cadastro_professor, name='cadastro_professor'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quiz/', views.quiz, name='quiz'),
    path('professor/', views.professor, name='professor'),
    path('professor/turmas/', views.listar_turmas, name='listar_turmas'),
    path('professor/turmas/cadastrar/', views.cadastrar_turma, name='cadastrar_turma'),
    path('professor/aluno/<int:aluno_id>/quiz/<int:resposta_id>/', views.detalhes_quiz_professor, name='detalhes_quiz_professor'),
    path('aluno/quiz/<int:resposta_id>/', views.detalhes_quiz_aluno, name='detalhes_quiz_aluno'),
]