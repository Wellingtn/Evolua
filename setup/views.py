from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import Aluno

def cadastro(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.senha = form.cleaned_data['senha']  # Salvar senha limpa (será ajustado depois para hashing)
            aluno.save()
            return redirect('/login/')  # Redireciona para a página de login
    else:
        form = AlunoForm()
    return render(request, 'cadastro.html', {'form': form})

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            aluno = Aluno.objects.get(email=email, senha=senha)  # Verifica credenciais
            request.session['aluno_id'] = aluno.id  # Armazena o ID na sessão
            return redirect('/dashboard/')  # Redireciona para o dashboard
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
    return render(request, 'quiz.html')

def professor(request):
    return render(request, 'professor.html')

