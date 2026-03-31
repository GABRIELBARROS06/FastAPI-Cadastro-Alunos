#Imports
from fastapi import APIRouter, HTTPException
from app.schemas.aluno import Aluno
import app.data.storage as storage

#Rotas do CRUD
router = APIRouter(prefix="/alunos", tags=["Alunos"])


#Listar todos os alunos presentes na lista
@router.get("/")
def listar_alunos():
    return {"alunos": storage.alunos}


#Criar um novo aluno na lista
@router.post("/")
def criar_aluno(aluno: Aluno):
    novo_aluno = {
        "id": storage.contador_id,
        "nome": aluno.nome,
        "email": aluno.email,
        "idade": aluno.idade,
        "curso": aluno.curso
    }
    #Será adicionado o aluno com os dados na lista
    storage.alunos.append(novo_aluno)
    #Sempre adicionará mais um
    storage.contador_id += 1

    return {
        "mensagem": "Aluno cadastrado com sucesso",
        "aluno": novo_aluno
    }

#Faz a busca do aluno no array, através do id_aluno
@router.get("/{aluno_id}")
def buscar_aluno(aluno_id: int):
    for aluno in storage.alunos:
        if aluno["id"] == aluno_id:
            return aluno

    #Tratamento de erro caso o Aluno não esteja cadastrado!
    raise HTTPException(status_code=404, detail="Aluno não encontrado")


#Atualiza os dados do aluno especifico através do id
@router.put("/{aluno_id}")
def atualizar_aluno(aluno_id: int, aluno_atualizado: Aluno):
    for aluno in storage.alunos:
        if aluno["id"] == aluno_id:
            aluno["nome"] = aluno_atualizado.nome
            aluno["email"] = aluno_atualizado.email
            aluno["idade"] = aluno_atualizado.idade
            aluno["curso"] = aluno_atualizado.curso

            return {
                "mensagem": "Aluno atualizado com sucesso",
                "aluno": aluno
            }

    raise HTTPException(status_code=404, detail="Aluno não encontrado")

#Deleta o aluno através do Id
@router.delete("/{aluno_id}")
def deletar_aluno(aluno_id: int):
    for aluno in storage.alunos:
        if aluno["id"] == aluno_id:
            storage.alunos.remove(aluno)
            return {"mensagem": "Aluno removido com sucesso"}

    raise HTTPException(status_code=404, detail="Aluno não encontrado")