from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Avg
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

def calcular_pontuacao(resposta):
    pontos = 0
    for i in range(1, 13):
        campo = f'resposta_{i}'
        valor = getattr(resposta, campo)
        if isinstance(valor, bool):
            pontos += 1 if valor else 0
        elif isinstance(valor, str) and valor.strip():
            pontos += 0.5
    return pontos

def dashboard(request):
    aluno_id = request.session.get('aluno_id')
    if not aluno_id:
        return redirect('setup:login')
    try:
        aluno = Aluno.objects.get(id=aluno_id)
        respostas = Resposta.objects.filter(aluno=aluno)
        
        # Calcular pontuação média
        pontuacoes = [calcular_pontuacao(r) for r in respostas]
        pontuacao_media = sum(pontuacoes) / len(pontuacoes) if pontuacoes else 0
        
        # Quantidade de quizzes respondidos
        quizzes_respondidos = respostas.count()
        
        # Atividades pendentes (assumindo que há 10 quizzes no total)
        total_quizzes = 10
        atividades_pendentes = total_quizzes - quizzes_respondidos
        
        # Progresso
        progresso = (quizzes_respondidos / total_quizzes) * 100 if total_quizzes > 0 else 0
        
        # Histórico de quizzes (últimos 5)
        historico_quizzes = [
            {'pilar': f'Quiz {i+1}', 'nota': calcular_pontuacao(r)}
            for i, r in enumerate(respostas.order_by('-id')[:5])
        ]
        
        # Dados para o gráfico
        meses = [f'Quiz {i+1}' for i in range(len(respostas))]
        notas = [calcular_pontuacao(r) for r in respostas]
        
        # Pilares FOIL (exemplo)
        pilares = [
            ('TRABALHO', 'Refere-se à importância de aplicar esforço prático para realizar objetivos. Através do trabalho, você aprende a se comprometer, assumir responsabilidades e desenvolver habilidades essenciais para crescer tanto pessoal quanto profissionalmente.'),
            ('ESTUDO', 'Representa o desenvolvimento contínuo do conhecimento e da inteligência. O estudo amplia suas capacidades técnicas e humanísticas, ajudando na resolução de problemas e na inovação, fundamentais para sua atuação no mercado e na sociedade.'),
            ('ALTA MORALIDADE', 'Envolve agir com ética, integridade e respeito pelos outros. A alta moralidade significa tomar decisões que não apenas beneficiam você, mas também o coletivo, sempre respeitando princípios elevados em todas as suas ações.'),
            ('INTERNACIONALIDADE', 'Envolve a abertura para novas culturas e formas de pensamento. A internacionalidade te prepara para atuar em um mundo globalizado, promovendo o intercâmbio de ideias e experiências que ampliam suas perspectivas e oportunidades.'),
            ('FOIL', 'Refere-se ao desenvolvimento da capacidade de compreensão e aplicação de conhecimentos interdisciplinares. Este pilar liga o indivíduo às suas experiências e ao mundo, permitindo uma formação integral que favorece a inovação e a solução criativa de problemas.')
        ]
        
        context = {
            'aluno': aluno,
            'progresso': progresso,
            'quizzes_respondidos': quizzes_respondidos,
            'atividades_pendentes': atividades_pendentes,
            'nota_media': pontuacao_media,
            'historico_quizzes': historico_quizzes,
            'meses': meses,
            'notas': notas,
            'pilares': pilares,
        }
        return render(request, 'dashboard.html', context)
    except Aluno.DoesNotExist:
        return redirect('setup:login')

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