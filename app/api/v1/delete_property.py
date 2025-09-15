from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Properties, Reservation

router = APIRouter()

@router.delete("/properties/{property_id}", status_code=204)
def delete_property(property_id: int = Path(..., description="ID da propriedade a ser deletada"),
                    db: Session = Depends(get_db)):

    property = db.query(Properties).filter(Properties.id == property_id).first()
    if not property:
        raise HTTPException(status_code=404, detail="Propriedade não encontrada")

    has_reservations = db.query(Reservation).filter(Reservation.property_id == property_id).first()
    if has_reservations:
        raise HTTPException(status_code=400, detail="Não é possível deletar propriedade com reservas associadas")

    db.delete(property)
    db.commit()