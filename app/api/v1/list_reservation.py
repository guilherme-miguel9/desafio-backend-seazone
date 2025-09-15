from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Reservation

router = APIRouter()

@router.get("/reservations", status_code = 200)
def list_reservations(property_id: int = Query(None, description="Informe o ID da propriedade para listar as reservas"),
                      client_email: str = Query(None, description="Informe o email do cliente para listar as reservas"),
                      db: Session = Depends(get_db)):
    
    if property_id:
        reservations_list = db.query(Reservation).filter(Reservation.property_id == property_id).all()
        return reservations_list

    if client_email:
        reservations_list = db.query(Reservation).filter(Reservation.client_email == client_email).all()
        return reservations_list
    
    
