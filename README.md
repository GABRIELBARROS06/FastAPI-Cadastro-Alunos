# 🚀 API de Alunos - FastAPI

Uma API REST desenvolvida em Python utilizando FastAPI para gerenciamento de alunos.

Este projeto faz parte dos meus estudos em desenvolvimento backend, com foco em construção de APIs, organização de código e boas práticas.

![Python](https://img.shields.io/badge/Python-3.14.3-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Tipo](https://img.shields.io/badge/Tipo-API%20REST-orange)
![Nível](https://img.shields.io/badge/Nível-Estudo-blueviolet)

---

## 📌 Objetivo

Criar uma API completa com operações CRUD (Create, Read, Update, Delete), evoluindo gradualmente para um sistema mais robusto com banco de dados e autenticação.

---

## 🛠️ Tecnologias utilizadas

- Python
- FastAPI
- Pydantic
- Uvicorn

---

## 📂 Estrutura do projeto
api-alunos/
├── app/
│ ├── main.py
│ ├── routes/
│ ├── schemas/
│ └── data/


---

## ⚙️ Funcionalidades atuais

✔️ Cadastro de alunos  
✔️ Listagem de alunos  
✔️ Busca por ID  
✔️ Atualização de dados  
✔️ Remoção de alunos  

---

## 🔗 Endpoints disponíveis

### 📍 Base
- `GET /` → Verifica se a API está funcionando

### 👨‍🎓 Alunos

- `GET /alunos/` → Lista todos os alunos  
- `POST /alunos/` → Cria um novo aluno  
- `GET /alunos/{id}` → Busca aluno por ID  
- `PUT /alunos/{id}` → Atualiza aluno  
- `DELETE /alunos/{id}` → Remove aluno  

---

## ▶️ Como executar o projeto

### 1. Clonar o repositório
git clone https://github.com/seu-usuario/api-alunos.git

## 2. Entrar na pasta
cd api-alunos

### 3. Criar ambiente virtual
python -m venv venv

### 4. Ativar ambiente virtual
venv\Scripts\activate

### 5. Instalar dependências
pip install fastapi uvicorn

### 6. Rodar a aplicação
fastapi dev app/main.py

---

📚 Documentação automática

Após rodar o projeto, acesse:

👉 http://127.0.0.1:8000/docs

A interface permite testar todos os endpoints diretamente no navegador.

---

🚧 Próximas melhorias

Este projeto ainda está em desenvolvimento e será evoluído com:

 Integração com banco de dados (SQLite / PostgreSQL)
 Uso de ORM (SQLAlchemy)
 Validação mais robusta dos dados
 Autenticação com JWT
 Deploy da API
 Estrutura mais avançada (services, controllers)

 ---

💡 Aprendizados

Durante o desenvolvimento deste projeto, estou aprendendo:

Estruturação de APIs REST
Organização de código em projetos backend
Uso do FastAPI
Validação de dados com Pydantic
Boas práticas de desenvolvimento

---

👨‍💻 Autor

Desenvolvido por Gabriel de Barros

🔗 GitHub: https://github.com/GABRIELBARROS06

🔗 LinkedIn: www.linkedin.com/in/gabriel-de-barros-gomes-067059314
