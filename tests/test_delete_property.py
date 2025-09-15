from fastapi.testclient import TestClient
import pytest
from app.main import app
from tests.test_create_properties import create_property
from tests.test_reservation_and_cancel import create_reservation

client = TestClient(app)

def test_delete_property_blocked_if_has_reservations(create_reservation):
    property_id = create_reservation["property_id"]

    delete_response = client.delete(f"/api/v1/properties/{property_id}")
    assert delete_response.status_code == 400

