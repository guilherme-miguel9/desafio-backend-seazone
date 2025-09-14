from pydantic import BaseModel
from datetime import date

# Esquema para criação de uma nova propriedade:
class PropertiesCreate(BaseModel):
    title: str
    address_street: str
    address_number: int
    address_neighborhood: str
    address_city: str
    address_state: str
    country: str
    rooms: int
    capacity: int
    price_per_night: int

    class Config:
        from_attributes = True

class PropertiesResponse(PropertiesCreate):
    id: int

    class Config:
        from_attributes = True

# Esquema para criação de uma nova reserva:
class ReservationCreate(BaseModel):
    property_id: int
    client_name: str
    client_email: str
    start_date: date
    end_date: date
    guests_quantity: int

    class Config:
        from_attributes = True