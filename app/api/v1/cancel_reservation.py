from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Reservation

router = APIRouter()

@router.delete("/cancel_reservation/", status_code=204)
def cancel_reservation(reservation_id: int = Query(..., description="ID da reserva para ser cancelada"),
                       db: Session = Depends(get_db)):
    
    reservation = db.query(Reservation).filter(Reservation.property_id == reservation_id).first()

    if not reservation:
        raise HTTPException(status_code=404, detail='Reserva nao foi encontrada')
    
    db.delete(reservation)
    db.commit()
    