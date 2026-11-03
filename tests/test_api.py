from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_literature():
    response = client.get("/api/v1/literature")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 8

def test_rag_search():
    response = client.post("/api/v1/rag/search", json={"query": "RAG DLP JKN", "top_k": 3})
    assert response.status_code == 200
    data = response.json()
    assert data["retrieved_count"] == 3
    assert len(data["results"]) == 3

def test_rag_generate():
    response = client.post("/api/v1/rag/generate")
    assert response.status_code == 200
    data = response.json()
    assert "markdown_path" in data
    assert "csv_path" in data
    assert "analysis_path" in data
