from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import or_, not_
from app.db.models import Reservation
from app.db.schemas import ReservationCreate
from app.db.schemas import ReservationResponse
from app.db.models import Properties


router = APIRouter()

@router.post("/reservation/", status_code=201, response_model=ReservationResponse)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):

    property = db.query(Properties).filter(Properties.id == reservation.property_id).first()
    #Verifica se a propriedade existe
    if not property:
        raise HTTPException(status_code=404, detail="Propriedade nao encontrada")
    
    #Verifica capacidade
    if reservation.guests_quantity > property.capacity:
        raise HTTPException(status_code=400, detail="Numero de hospedes excedeu a capacidade da propriedade.")
    
    #Verifica conflitos de datas
    if reservation.end_date <= reservation.start_date:
        raise HTTPException(status_code=400, detail="Data de termino deve ser maior que a data de inicio")
    
    conflicting_reservation = db.query(Reservation).filter(
        Reservation.property_id == reservation.property_id,
        Reservation.end_date >= reservation.start_date,
        Reservation.start_date <= reservation.end_date
    ).first()
    if conflicting_reservation:
        raise HTTPException(status_code=400, detail="A propriedade já estava reservada para as datas selecionadas")
    
    #Calcula o valor total para a reserva
    total_days = (reservation.end_date - reservation.start_date).days
    total_price = total_days * property.price_per_night



    new_reservation = Reservation(
        property_id=reservation.property_id,
        client_name=reservation.client_name,
        client_email=reservation.client_email,
        start_date=reservation.start_date,
        end_date=reservation.end_date,
        guests_quantity=reservation.guests_quantity,
        total_price=total_price  
    )

    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation
