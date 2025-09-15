import pytest
from fastapi.testclient import TestClient
from app.main import app
from tests.test_create_properties import create_property

client = TestClient(app)


def test_list_all_properties(create_property):
    response = client.get("/api/v1/list_properties/?list_all=true")
    assert response.status_code == 200
    data = response.json()
    assert any(p["id"] == create_property["id"] for p in data)

def test_filter_by_neighborhood(create_property):
    neighborhood = create_property["address_neighborhood"]
    response = client.get(f"/api/v1/list_properties/?neighborhood={neighborhood}")
    assert response.status_code == 200
    data = response.json()
    assert all(neighborhood.lower() in p["address_neighborhood"].lower() for p in data)
    assert any(p["id"] == create_property["id"] for p in data)

def test_filter_by_capacity(create_property):
    capacity = create_property["capacity"]
    response = client.get(f"/api/v1/list_properties/?capacity={capacity}")
    assert response.status_code == 200
    data = response.json()
    assert all(p["capacity"] >= capacity for p in data)
    assert any(p["id"] == create_property["id"] for p in data)

def test_filter_by_price_max(create_property):
    price_max = create_property["price_per_night"]
    response = client.get(f"/api/v1/list_properties/?price_max={price_max}")
    assert response.status_code == 200
    data = response.json()
    assert all(p["price_per_night"] <= price_max for p in data)
    assert any(p["id"] == create_property["id"] for p in data)