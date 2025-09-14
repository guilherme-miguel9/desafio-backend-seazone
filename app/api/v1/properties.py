from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db  
from app.db.models import Properties
from app.db.schemas import PropertiesCreate
from app.db.schemas import PropertiesResponse

router = APIRouter()

@router.post("/properties/", status_code=201, response_model=PropertiesResponse)
def create_property(property: PropertiesCreate, db: Session = Depends(get_db)):
    new_property = Properties(
        title=property.title,
        address_street=property.address_street,
        address_number=property.address_number,
        address_neighborhood=property.address_neighborhood,
        address_city=property.address_city,
        address_state=property.address_state,
        country=property.country,
        rooms=property.rooms,
        capacity=property.capacity,
        price_per_night=property.price_per_night
    )
    
    db.add(new_property)
    db.commit()
    db.refresh(new_property)
    return new_property
