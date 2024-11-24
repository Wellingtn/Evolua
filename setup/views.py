from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AlunoForm, ProfessorForm, RespostaForm
from .models import Aluno, Professor, Turma, Resposta

def cadastro(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.senha = form.cleaned_data['senha']  # Lembre-se de implementar o hashing da senha
            aluno.save()
            return redirect('setup:login')
    else:
        form = AlunoForm()
    return render(request, 'cadastro.html', {'form': form})

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            aluno = Aluno.objects.get(email=email, senha=senha)  # Implemente autenticação segura
            request.session['aluno_id'] = aluno.id
            return redirect('setup:dashboard')
        except Aluno.DoesNotExist:
            messages.error(request, "E-mail ou senha inválidos.")
    return render(request, 'login.html')

def dashboard(request):
    aluno_id = request.session.get('aluno_id')
    if not aluno_id:
        return redirect('setup:login')
    try:
        aluno = Aluno.objects.get(id=aluno_id)
    except Aluno.DoesNotExist:
        return redirect('setup:login')
    return render(request, 'dashboard.html', {'aluno': aluno})

def quiz(request):
    aluno_id = request.session.get('aluno_id')
    if not aluno_id:
        return redirect('setup:login')
    
    if request.method == "POST":
        form = RespostaForm(request.POST)
        if form.is_valid():
            resposta = form.save(commit=False)
            resposta.aluno_id = aluno_id
            resposta.save()
            return redirect('setup:dashboard')
    else:
        form = RespostaForm()
    
    return render(request, 'quiz.html', {'form': form})

def cadastro_professor(request):
    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            professor = form.save(commit=False)
            professor.senha = form.cleaned_data['senha']  # Lembre-se de implementar o hashing da senha
            professor.save()
            return redirect('setup:login')
    else:
        form = ProfessorForm()
    return render(request, 'cadastro_professor.html', {'form': form})

def professor(request):
    # Implemente a lógica para a página do professor
    return render(request, 'professor.html')

