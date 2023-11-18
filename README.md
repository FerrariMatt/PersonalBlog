# Django Development Project

This repository contains a project of a Personal Blog, that contains a user creation and authentication project. When logged the User will have access to a To-Do List, to manage and create their own tasks. The main objective of this project is to establish a solid foundation for web application development using the Django framework, putting acquired knowledge into practice and thereby evolving as a developer.

The Front-End is developed using Bootstrap.

## Application operation video



## Environment Setup

Make sure you have Python and pip installed on your system. It is recommended to use virtual environments to isolate project dependencies. To set up the environment, follow the steps below:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/FerrariSnow/PersonalBlog.git
   cd PersonalBlog
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Database Configuration

This project is configured to use SQLite by default. If you want to use another database, adjust the settings in the `settings.py` file as needed.

Run migrations to apply changes to the database:
```bash
python manage.py migrate
```

## Running the Development Server

Start the development server with the following command:
```bash
python manage.py runserver
```

Access the project at [http://localhost:8000/](http://localhost:8000/).

## Contributing

Feel free to contribute to this project. Before submitting a pull request, make sure to follow the contribution guidelines.

## Main Directories

- **PersonalBlog/**
  - **PersonalBlog/**
    - `settings.py`: Project settings.
    - `urls.py`: Routing configurations.
  - `manage.py`: Django command-line utility.
  - `requirements.txt`: List of project dependencies.
  - `venv/`: Virtual environment (can be ignored if you are not using a virtual environment).
  - `README.md`: This file.

## Issues or Questions?

If you encounter issues or have questions, please open an issue on GitHub.

Thank you for reading this far; have a great day ! :v:



# Projeto Django em Desenvolvimento

Este repositório contém um projeto de um Blog Pessoal, que contem criação e autenticação de usuário. Quando logado, o usuário terá acesso a um To-Do List, para gerenciar e criar suas próprias tarefas. O objetivo principal deste projeto é adquirir uma base sólida para o desenvolvimento de aplicações web usando o framework Django, botando em prática o conhecimento adquirido e com isso evoluir como desenvolvedor.

Front-End desenvolvido utilizando Bootstrap.

## Vídeo de funcionamento da aplicação



## Configuração do Ambiente

Certifique-se de ter o Python e o pip instalados em seu sistema. Recomenda-se o uso de ambientes virtuais para isolar as dependências do projeto. Para configurar o ambiente, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/FerrariSnow/PersonalBlog.git
   cd PersonalBlog
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuração do Banco de Dados

Este projeto está configurado para usar o SQLite por padrão. Se você deseja usar outro banco de dados, ajuste as configurações no arquivo `settings.py` conforme necessário.

Execute as migrações para aplicar as alterações ao banco de dados:
```bash
python manage.py migrate
```

## Executando o Servidor de Desenvolvimento

Inicie o servidor de desenvolvimento com o seguinte comando:
```bash
python manage.py runserver
```

Acesse o projeto em [http://localhost:8000/](http://localhost:8000/).

## Contribuindo

Sinta-se à vontade para contribuir para este projeto. Antes de enviar um pull request, certifique-se de seguir as diretrizes de contribuição.

## Diretórios Principais

- **PersonalBlog/**
  - **PersonalBlog/**
    - `settings.py`: Configurações do projeto.
    - `urls.py`: Configurações de roteamento.
  - `manage.py`: Utilitário de linha de comando do Django.
  - `requirements.txt`: Lista de dependências do projeto.
  - `venv/`: Ambiente virtual (pode ser ignorado se você não estiver usando um ambiente virtual).
  - `README.md`: Este arquivo.

## Problemas ou Dúvidas?

Se você encontrar problemas ou tiver dúvidas, por favor, abra uma issue no GitHub.

Obrigado por ler até aqui, tenha um ótimo dia ! :v:
