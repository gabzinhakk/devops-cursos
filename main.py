from fastapi import FastAPI

app = FastAPI()

cursos = [
    {"id": 1, "nome": "NR-35 Trabalho em Altura"},
    {"id": 2, "nome": "NR-10 Segurança em Eletricidade"}
]

@app.get("/")
async def root():
    return {
        "api": "Treinamentos de Segurança",
        "status": "online"
    }

@app.get("/cursos")
async def listar_cursos():
    return cursos

@app.get("/cursos/{id}")
async def buscar_curso(id: int):
    for curso in cursos:
        if curso["id"] == id:
            return curso
    return {"erro": "Curso não encontrado"}