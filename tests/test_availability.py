from fastapi.testclient import TestClient
import pytest
from app.main import app
from tests.test_reservation_and_cancel import create_reservation

client = TestClient(app)

def test_availability_with_conflict(create_reservation):
    response = client.get(
        "/api/v1/properties/availability",
        params={
            "property_id": 1,
            "start_date": "2024-12-20",
            "end_date": "2024-12-27"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["available"] is False

def test_availability_no_conflict():
    response = client.get(
        "/api/v1/properties/availability",
        params={
            "property_id": 1,
            "start_date": "2025-01-01",
            "end_date": "2025-01-05"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["available"] is True