from fastapi import FastAPI
from app.api.v1 import properties, list_properties, reservation, list_reservation

app = FastAPI()

app.include_router(properties.router, prefix="/api/v1")
app.include_router(list_properties.router, prefix="/api/v1")
app.include_router(reservation.router, prefix="/api/v1")
app.include_router(list_reservation.router, prefix="/api/v1")