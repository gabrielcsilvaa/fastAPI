from fastapi import FastAPI
from pydantic import BaseModel

bdLivros = {}

class Livros(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int
    preco: float
    disponibilidade: bool

app = FastAPI()

@app.get("/")
def mostrarInfo:
    return{
        "mensagem": "Api De Livros",
        "versao": "1.0"
    }

@app.get("/Livros/")
def mostrarTodosLivros():
    return {
        "Livros": bdLivros,
        "statusCode": 200

    }
@app.get("/Livros/{id}")
def mostrarUmLivro(id: int):
    try:
        return{
            "Livro": bdLivros[id],
            "statusCode": 200
    }
    except:
        return {
            "livro": "livro nao encontrado"
            "statusCode": 404
        }