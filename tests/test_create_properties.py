from fastapi.testclient import TestClient
import pytest
from app.main import app

client = TestClient(app)

# Teste de criação de uma nova propriedade, utilizei valores ficticios do proprio desafio.
@pytest.fixture
def create_property():
    payload = {
        "title": "Casa de Férias Algarve",
        "address_street": "Av Github",
        "address_number": 2024,
        "address_neighborhood": "Jurerê", 
        "address_city": "Florianópolis", 
        "address_state": "SC", 
        "country": "BRA", 
        "rooms": 3, 
        "capacity": 6, 
        "price_per_night": 120.00 
    }

    response = client.post("/api/v1/properties/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["address_number"] == payload["address_number"]
    assert "id" in data
    return data