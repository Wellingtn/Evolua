from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Avg
from .forms import AlunoForm, ProfessorForm, RespostaForm, TurmaForm
from .models import Aluno, Professor, Turma, Resposta
from django.contrib.auth.hashers import make_password, check_password


def seleciona_usuario(request):
    return render(request, 'selecionar_usuario.html')

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

def login_professor(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            professor = Professor.objects.get(email=email)
            if check_password(senha, professor.senha):
                request.session['professor_id'] = professor.id
                return redirect('setup:professor')
            else:
                messages.error(request, "E-mail ou senha inválidos.")
        except Professor.DoesNotExist:
            messages.error(request, "E-mail ou senha inválidos.")
    return render(request, 'login_professor.html')

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
        
        # Atualizar o histórico de quizzes para incluir o ID da resposta
        historico_quizzes = [
            {'id': r.id, 'pilar': f'Quiz {i+1}', 'nota': calcular_pontuacao(r)}
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
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if Professor.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está cadastrado.")
        else:
            professor = Professor(
                nome=nome,
                email=email,
                senha=make_password(senha)
            )
            professor.save()
            messages.success(request, "Professor cadastrado com sucesso!")
            return redirect('setup:login')  # Redireciona para a página de login após o cadastro

    return render(request, 'cadastro_professor.html')

# ... (manter as outras funções existentes)



def professor(request):
    professor_id = request.session.get('professor_id')
    if not professor_id:
        return redirect('setup:login_professor')
    
    try:
        professor = Professor.objects.get(id=professor_id)
        turmas = Turma.objects.filter(professor=professor)
        
        selected_turma_id = request.GET.get('turma')
        
        total_cursos = turmas.count()
        total_alunos = sum(turma.alunos.count() for turma in turmas)
        
        pilares = ['Trabalho', 'Estudo', 'Alta Moralidade', 'Internacionalidade', 'FOIL']
        medias_pilares = {pilar: 0 for pilar in pilares}
        
        alunos_count = 0 # Update 1: Added alunos_count
        
        alunos_info = []
        for turma in turmas:
            if selected_turma_id and int(selected_turma_id) != turma.id_turma:
                continue
            for aluno in turma.alunos.all():
                respostas = Resposta.objects.filter(aluno=aluno)
                if respostas.exists():
                    ultima_resposta = respostas.latest('id')
                    
                    # Calculate individual pillar scores
                    trabalho = (ultima_resposta.resposta_1 or 0) + (ultima_resposta.resposta_2 or 0)
                    estudo = (ultima_resposta.resposta_3 or 0) + (0.5 if ultima_resposta.resposta_4 else 0)
                    alta_moralidade = (ultima_resposta.resposta_5 or 0) + (ultima_resposta.resposta_6 or 0)
                    internacionalidade = (ultima_resposta.resposta_7 or 0) + (ultima_resposta.resposta_8 or 0)
                    foil = (0.5 if ultima_resposta.resposta_9 else 0) + (ultima_resposta.resposta_10 or 0) + \
                           (0.5 if ultima_resposta.resposta_11 else 0) + (0.5 if ultima_resposta.resposta_12 else 0)
                    
                    notas_pilares = [trabalho, estudo, alta_moralidade, internacionalidade, foil]
                    total_pontos_aluno = sum(notas_pilares)
                    
                    alunos_count += 1 # Update 2: Incremented alunos_count
                    
                    alunos_info.append({
                        'id': aluno.id,
                        'nome': f"{aluno.nome} {aluno.sobrenome}",
                        'notas_pilares': notas_pilares,
                        'total_pontos': total_pontos_aluno,
                        'ultima_resposta_id': ultima_resposta.id,
                        'turma_nome': turma.nome
                    })
                    
                    for i, pilar in enumerate(pilares):
                        medias_pilares[pilar] += notas_pilares[i]
        
        # Calculando a média de pontos para cada pilar # Update 3: Replaced calculation
        for pilar in pilares:
            medias_pilares[pilar] = round(medias_pilares[pilar] / alunos_count if alunos_count > 0 else 0, 2)
        
        context = {
            'professor': professor,
            'turmas': turmas,
            'selected_turma_id': int(selected_turma_id) if selected_turma_id else None,
            'total_cursos': total_cursos,
            'total_alunos': total_alunos,
            'medias_pilares': medias_pilares,
            'alunos_info': alunos_info
        }
        
        return render(request, 'professor.html', context)
    except Professor.DoesNotExist:
        return redirect('setup:login_professor')


def cadastrar_turma(request):
    professor_id = request.session.get('professor_id')
    if not professor_id:
        return redirect('setup:login_professor')

    professor = get_object_or_404(Professor, id=professor_id)

    if request.method == "POST":
        form = TurmaForm(request.POST, professor=professor)
        if form.is_valid():
            turma = form.save()
            messages.success(request, f"Turma '{turma.nome}' cadastrada com sucesso!")
            return redirect('setup:listar_turmas')
    else:
        form = TurmaForm(professor=professor)

    return render(request, 'cadastrar_turma.html', {'form': form})

def listar_turmas(request):
    professor_id = request.session.get('professor_id')
    if not professor_id:
        return redirect('setup:login_professor')

    professor = get_object_or_404(Professor, id=professor_id)
    turmas = Turma.objects.filter(professor=professor)

    return render(request, 'listar_turmas.html', {'turmas': turmas})

def detalhes_quiz_professor(request, aluno_id, resposta_id):
    professor_id = request.session.get('professor_id')
    if not professor_id:
        return redirect('setup:login_professor')

    professor = get_object_or_404(Professor, id=professor_id)
    aluno = get_object_or_404(Aluno, id=aluno_id)
    resposta = get_object_or_404(Resposta, id=resposta_id, aluno=aluno)

    context = {
        'professor': professor,
        'aluno': aluno,
        'resposta': resposta,
    }
    return render(request, 'detalhes_quiz_professor.html', context)

def detalhes_quiz_aluno(request, resposta_id):
    aluno_id = request.session.get('aluno_id')
    if not aluno_id:
        return redirect('setup:login')

    aluno = get_object_or_404(Aluno, id=aluno_id)
    resposta = get_object_or_404(Resposta, id=resposta_id, aluno=aluno)

    context = {
        'aluno': aluno,
        'resposta': resposta,
    }
    return render(request, 'detalhes_quiz_aluno.html', context)