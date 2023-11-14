# Projeto Django em Desenvolvimento

Este repositório contém um projeto de criação e autenticação de usuário, o objetivo principal deste projeto é adquirir uma base sólida para o desenvolvimento de aplicações web usando o framework Django.

Front-End desenvolvido utilizando Bootstrap.

## Configuração do Ambiente

Certifique-se de ter o Python e o pip instalados em seu sistema. Recomenda-se o uso de ambientes virtuais para isolar as dependências do projeto. Para configurar o ambiente, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/FerrariSnow/UserAuthentication.git
   cd UserAuthentication
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

- **UserAuthentication/**
  - **UserAuthentication/**
    - `settings.py`: Configurações do projeto.
    - `urls.py`: Configurações de roteamento.
  - `manage.py`: Utilitário de linha de comando do Django.
  - `requirements.txt`: Lista de dependências do projeto.
  - `venv/`: Ambiente virtual (pode ser ignorado se você não estiver usando um ambiente virtual).
  - `README.md`: Este arquivo.

## Problemas ou Dúvidas?

Se você encontrar problemas ou tiver dúvidas, por favor, abra uma issue no GitHub.

Obrigado por ler até aqui, tenha um ótimo dia ! :v: