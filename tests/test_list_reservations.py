import pytest
from fastapi.testclient import TestClient
from app.main import app
from tests.test_reservation_and_cancel import create_reservation

client = TestClient(app)

def test_list_reservations_by_property(create_reservation):
    property_id = create_reservation["property_id"]
    response = client.get(f"/api/v1/list_reservations/?property_id={property_id}")
    assert response.status_code == 200
    reservations = response.json()
    assert isinstance(reservations, list)
    assert any(r["id"] == create_reservation["id"] for r in reservations)

def test_list_reservations_by_email(create_reservation):
    client_email = create_reservation["client_email"]
    response = client.get(f"/api/v1/list_reservations/?client_email={client_email}")
    assert response.status_code == 200
    reservations = response.json()
    assert any(r["id"] == create_reservation["id"] for r in reservations)