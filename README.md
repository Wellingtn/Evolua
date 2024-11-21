# Evolua

## Oque falta:
    - Mensagem de erro quando o usuario tenta fazer login sem ter uma conta (Login)
    - Ajustes na tela de cadastro (Cadastro)
    - Pilares Foil (Dashboard)
    - Rota semestres (Dashboard)
    - Tabela no banco de dados para as respostas do questionario (Questionario)
    - Calculo de notas do Dashboard (Dashboard)

## Oque foi feito:
    - Login e cadastro funcional (Login e Cadastro)
    - Tela de Dashboard com os dados do usuario (Dashboard)
    - Templates: Cadastro, Login, Dashboard, Questionario, Professor 
    - Connexão com o banco de dados (Banco de dados)


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
