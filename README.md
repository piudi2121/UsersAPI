<img width="1919" height="764" alt="Captura de tela 2026-02-10 141334" src="https://github.com/user-attachments/assets/7afcd080-822f-490d-a337-d6c5b76fe1bc" />

# Users API

API simples para gerenciamento de usuários utilizando FastAPI, SQLAlchemy e SQLite.  
Projeto focado em estudo de integração entre API e banco de dados.

## Funcionalidades

- Criar usuário
- Buscar usuário por ID
- Listar todos os usuários
- Atualizar usuário
- Remover usuário

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Como rodar o projeto

1. Clone o repositório
2. Entre na pasta do projeto
3. Instale os pacotes necessários:

```bash
pip install fastapi uvicorn sqlalchemy
```
```bash
uvicorn main:app --reload
```

## Endpoints principais

* POST `/users` — cria um usuário
* GET `/users` — lista usuários
* GET `/users/{id}` — busca usuário por ID
* PUT `/users/{id}` — atualiza usuário
* DELETE `/users/{id}` — remove usuário

## Observações

* O banco de dados SQLite é criado automaticamente ao rodar a aplicação
* Validação de email é feita com `EmailStr` do Pydantic
