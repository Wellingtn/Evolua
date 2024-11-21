from django.urls import path
from . import views

app_name = 'setup'  # Certifique-se de usar o nome correto do app
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Preparado para a próxima etapa
    path('quiz/', views.quiz, name='quiz'),
    path('professor/', views.professor, name='professor'),
]
