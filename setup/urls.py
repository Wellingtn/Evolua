from django.urls import path
from . import views

app_name = 'setup'
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quiz/', views.quiz, name='quiz'),
    path('professor/', views.professor, name='professor'),
    path('cadastro_professor/', views.cadastro_professor, name='cadastro_professor'),
]

