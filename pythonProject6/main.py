from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#rota principal de apresentacao

class Produto(BaseModel):
    nome: str
    preco: float


bancoDados = {
    1:{
        "nome":"pizza",
        "preco" : 59.90
    },
    2:{
        "lasanha": "Lasanha",
        "preço": 9.90
    }
}



@app.get("/")
def apresentacao9():
    return {

       "mensagem": "ola mundo",
        "statusCode": 200
    }

@app.get("/{nome}")
def saudacao(nome):
    return {
        "mensagem": f'Ola {nome}',
        "statusCode": 200
    }

@app.get("/produtos/")
def MostrarTodosProdutos():
    return bancoDados

@app.get("/produtos/{idProduto}")
def mostarUmproduto(idProduto):
    try:
        if bancoDados[idProduto]:
            return {
                "produto": bancoDados[idProduto],
                "statusCode": 200
            }
    except:
        return{
            "produto": "nao encontrado",
            "statusCode": 404

        }

@app.post("/produto/cadastrar/{id}/produto")
def cadastrarProduto(id: int, item: Produto):
    id = len(bancoDados)+1
    bancoDados[id]= item
    return {
        "mensagem": "item criado com sucesso",
        "Produto": item,
        "statusCode": 200
    }

@app.delete("/produtos/excluir/{id}")
def excluirProduto(id):
    del bancoDados[id]
    return {
        "mensagem": "Produto excluido",
        "id produto": id,
        "statusCode": 200
    }