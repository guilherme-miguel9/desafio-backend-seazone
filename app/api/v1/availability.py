from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, not_
from app.db.database import get_db
from app.db.models import Reservation
from datetime import date

router = APIRouter()


@router.get("/properties/availability", status_code=200)
def check_availability(property_id: int = Query(..., description="ID da propriedade para verificar disponibilidade"),
                       start_date: date = Query(..., description="Data de início no formato YYYY-MM-DD"),
                       end_date: date = Query(..., description="Data de término no formato YYYY-MM-DD"),
                       db: Session = Depends(get_db)):
    
    conflicting_reservation = db.query(Reservation).filter(
        Reservation.property_id == property_id,
        not_(
            or_(
                Reservation.end_date < start_date,
                Reservation.start_date > end_date
            )
        )
    ).first()
    
    if conflicting_reservation:
        return {"available": False, "message": "Não há disponibilidade de propriedade para as datas selecionadas"}
    
    return {"available": True, "message": "A propriedade está disponível para as datas selecionadas"}