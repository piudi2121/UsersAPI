<img width="1919" height="798" alt="image" src="https://github.com/user-attachments/assets/5bd5740a-fdea-464b-a536-86c614581fca" />

---

# Users API

API para gerenciamento de usuários desenvolvida com FastAPI, SQLAlchemy e SQLite.

O projeto foi estruturado utilizando **arquitetura em camadas (Layered Architecture)**.

Essa separação melhora a organização, testabilidade e manutenção do código.

Além disso, a aplicação implementa **autenticação baseada em JWT (JSON Web Token)** para proteger as rotas de usuário.

---

## Funcionalidades

* Criar usuário
* Buscar usuário por ID
* Listar todos os usuários
* Atualizar usuário
* Remover usuário
* Autenticação via JWT
* Proteção das rotas `/users` utilizando token válido

---

## Tecnologias

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT
* Pydantic

---

## Autenticação

A autenticação foi implementada utilizando **JWT**.

Fluxo de autenticação:

1. O usuário realiza login.
2. A API gera um **access token JWT**.
3. O cliente deve enviar o token no header:

```
Authorization: Bearer <seu_token>
```

As rotas relacionadas a `/users` estão protegidas e exigem token válido para acesso.

---

## Como rodar o projeto

1. Clone o repositório
2. Entre na pasta do projeto
3. Instale os pacotes necessários:

```bash
pip install fastapi uvicorn sqlalchemy pyjwt bcrypt python-dotenv
```

4. Execute a aplicação:

```bash
uvicorn main:app --reload
```

---

## Endpoints principais

### 🔐 Autenticação

* POST `/api/auth/token` — realiza autenticação e retorna JWT

### 👤 Usuários (rotas protegidas)

* POST `/users` — cria um usuário
* GET `/users` — lista usuários
* GET `/users/{id}` — busca usuário por ID
* PUT `/users/{id}` — atualiza usuário
* DELETE `/users/{id}` — remove usuário

---

## Observações

* O banco de dados SQLite é criado automaticamente ao rodar a aplicação
* Validação de email é feita com `EmailStr` do Pydantic
* As rotas de usuários exigem autenticação via JWT

