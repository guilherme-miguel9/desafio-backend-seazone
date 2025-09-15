from fastapi import FastAPI
from app.api.v1 import properties, list_properties, reservation, list_reservation, cancel_reservation, availability, delete_property

app = FastAPI()

prefix = "/api/v1"

app.include_router(properties.router, prefix=prefix)
app.include_router(list_properties.router, prefix=prefix)
app.include_router(reservation.router, prefix=prefix)
app.include_router(list_reservation.router, prefix=prefix)
app.include_router(cancel_reservation.router, prefix=prefix)
app.include_router(availability.router, prefix=prefix)
app.include_router(delete_property.router, prefix=prefix)