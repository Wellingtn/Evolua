# Evolua

## Oque falta:
    
## Oque foi feito:
    - Login e cadastro funcional (Login e Cadastro)
    - Tela de Dashboard com os dados do usuario (Dashboard)
    - Templates: Cadastro, Login, Dashboard, Questionario, Professor 
    - Connexão com o banco de dados (Banco de dados)
    - Mensagem de erro quando o usuario tenta fazer login sem ter uma conta (Login)
        - Não mostra erro, mas não quebra o código
    - Calculo de notas do Dashboard (Dashboard)
    - Tabela no banco de dados para as respostas do questionario (Questionario)
    - Pilares Foil (Dashboard)
    - Fazer os alunos ficarem na turma(Banco de dados)
    - Fazer aparecer as turmas de certo professor(Dashboard Proofessor)
    - Ajustes na tela de selecionar usuario(selecao)
    - Ajustes na tela de cadastro (Cadastro)
    - Fazer aparecer os formularios já respondidos (Dashboard)
    -ajustar turmas no dashboard do profefessor (Dashboard Professor)
    -Ajustar templates de cadatro de turma
    -Ajustar templates de listagem de turmas
  

## Como rodar o projeto:
    1. Clone o repositorio
        git clone git@github.com:Wellingtn/Evolua.git
    2. Crie um ambiente virtual
        python -m venv venv
    3. Ative o ambiente virtual
        venv\Scripts\activate
    4. Instale o Django no ambiente virtual
        pip install django
    5. Instale as dependencias
        pip install -r requirements.txt
    6. Mirage o banco de dados
        python manage.py migrate
    7. Rode o comando python manage.py runserver
        python manage.py runserver
