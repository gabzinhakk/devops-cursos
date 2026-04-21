from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_listar_cursos():
    response = client.get("/cursos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_buscar_curso():
    response = client.get("/cursos/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1