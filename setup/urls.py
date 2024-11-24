from django.urls import path
from . import views

app_name = 'setup'
urlpatterns = [
    path('', views.seleciona_usuario, name='seleciona_usuario'),
    path('login/aluno/', views.login, name='login'),
    path('login/professor/', views.login_professor, name='login_professor'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro_professor/', views.cadastro_professor, name='cadastro_professor'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quiz/', views.quiz, name='quiz'),
    path('professor/', views.professor, name='professor'),
    path('professor/turmas/', views.listar_turmas, name='listar_turmas'),
    path('professor/turmas/cadastrar/', views.cadastrar_turma, name='cadastrar_turma'),
    path('professor/aluno/<int:aluno_id>/', views.detalhes_aluno, name='detalhes_aluno'),

]