# Projeto FastAPI - Aprendendo Conceitos Fundamentais

Este repositório contém um projeto desenvolvido com o objetivo de aprender e aplicar conceitos fundamentais do FastAPI, um framework moderno e rápido (high-performance) para construção de APIs com Python. O projeto inclui integração com MongoDB para persistência de dados, autenticação JWT (JSON Web Tokens), e operações CRUD (Create, Read, Update, Delete) para gerenciamento de usuários e tarefas.

## Tecnologias Utilizadas
- FastAPI: Framework para construção da API.

- MongoDB: Banco de dados NoSQL para armazenamento de dados.

- Motor: Driver assíncrono para MongoDB.

- Beanie: ODM (Object Document Mapper) para MongoDB, baseado em Pydantic.

- JWT: Autenticação baseada em tokens.

- Docker: Containerização do MongoDB e Mongo Express.

## Endpoints da API
### Auth
- ```POST /auth/login```: Realiza o login e retorna tokens de acesso e refresh.

- ```POST /auth/test-token```: Testa o token de acesso e retorna os detalhes do usuário autenticado.

## Users
- ```POST /users/register```: Registra um novo usuário.

## Tasks
- ```GET /tasks```: Lista todas as tarefas do usuário autenticado.

- ```GET /tasks/{task_id}```: Obtém uma tarefa específica pelo ID.

- ```POST /tasks```: Cria uma nova tarefa.

- ```PUT /tasks/{task_id}```: Atualiza uma tarefa existente.

- ```DELETE /tasks/{task_id}```: Remove uma tarefa.
