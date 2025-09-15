from fastapi.testclient import TestClient
import pytest
from app.main import app
from sqlalchemy.orm import Session
from app.db.models import Reservation
from app.db.database import SessionLocal
from tests.test_create_properties import create_property

client = TestClient(app)

@pytest.fixture
def create_reservation(create_property):
    property_id = create_property["id"]

    payload = {
        "property_id": property_id,
        "client_name": "Maria Pereira",
        "client_email": "mariapereira@example.com",
        "start_date": "2024-12-20",
        "end_date": "2024-12-27",
        "guests_quantity": 4
    }
    response = client.post("/api/v1/reservation/", json=payload)
    assert response.status_code == 201
    reservation_data = response.json()
    

    yield reservation_data

    reservation_id = reservation_data["id"]

    with SessionLocal() as db:
        reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
        if reservation:
            db.delete(reservation)
            db.commit()

   
def test_cancel_reservation(create_reservation):
    reservation_id = create_reservation["id"]

    response = client.delete(f"/api/v1/reservation/{reservation_id}")
    assert response.status_code == 204

    with SessionLocal() as db:
        reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
        
    assert reservation is None