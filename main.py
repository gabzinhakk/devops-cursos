from fastapi import FastAPI

app = FastAPI()

cursos = [
    {"id": 1, "nome": "NR-35 Trabalho em Altura"},
    {"id": 2, "nome": "NR-10 Segurança em Eletricidade"}
]

@app.get("/")
async def root():
    return {"message": "API de Treinamentos"}

@app.get("/cursos")
async def listar_cursos():
    return cursos