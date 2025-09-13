from pydantic import BaseModel


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
        orm_mode = True