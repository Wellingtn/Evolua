from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .forms import AlunoForm
from .models import Aluno
from django.shortcuts import render
from datetime import datetime
from .models import Pilar

def cadastro(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.senha = make_password(form.cleaned_data['senha'])  # Usando hashing para salvar a senha
            aluno.save()
            request.session['aluno_id'] = aluno.id  # Armazenando o ID do aluno na sessão
            return redirect('/dashboard/')  # Redireciona para o dashboard após cadastro
    else:
        form = AlunoForm()
    return render(request, 'cadastro.html', {'form': form})

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            aluno = Aluno.objects.get(email=email)  # Encontra o aluno pelo e-mail
            if check_password(senha, aluno.senha):  # Compara a senha informada com a senha armazenada
                request.session['aluno_id'] = aluno.id  # Armazena o ID na sessão
                return redirect('/dashboard/')  # Redireciona para o dashboard
            else:
                messages.error(request, "E-mail ou senha inválidos.")
        except Aluno.DoesNotExist:
            messages.error(request, "E-mail ou senha inválidos.")
    return render(request, 'login.html')

def dashboard(request):
    aluno_id = request.session.get('aluno_id')  # Pega o ID do aluno na sessão
    if not aluno_id:
        return redirect('setup:login')  # Redireciona para o login se não estiver autenticado

    try:
        aluno = Aluno.objects.get(id=aluno_id)
    except Aluno.DoesNotExist:
        return redirect('setup:login')  # Redireciona se o ID não for encontrado

    return render(request, 'dashboard.html', {'aluno': aluno})

def quiz(request):
    pilars = Pilar.objects.prefetch_related('perguntas__opcoes').all()
    return render(request, 'quiz.html', {'pilars': pilars, 'year': datetime.now().year})

def professor(request):
    return render(request, 'professor.html')
