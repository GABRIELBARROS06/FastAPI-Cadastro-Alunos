from fastapi import FastAPI
from app.routes.aluno_routes import router as aluno_router

app = FastAPI(
    title="API de Alunos",
    description="API para cadastro e gerenciamento de alunos",
    version="1.0.0"
)

app.include_router(aluno_router)


@app.get("/")
def inicio():
    return {"mensagem": "API funcionando com sucesso!"}