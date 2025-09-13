from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Properties


router = APIRouter()

# Listar propriedades do bd
@router.get("/list_properties/", status_code=200)
def list_properties(list_all: bool = Query(False, description="Selecione entre True ou False para listar todas as propriedades ou não"),
                    neighborhood: str = Query(None, description="Filtrar propriedades por bairro"),
                    city: str = Query(None, description="Filtrar propriedades por cidade"),
                    state: str = Query(None, description="Filtrar propriedades por estado"),
                    capacity: int = Query(None, description="Filtrar propriedades por capacidade"),
                    price_max: float = Query(None, description="Filtrar propriedades por preço máximo"),
                    db: Session = Depends(get_db)):
    if list_all:
        properties_list = db.query(Properties).all()
        return properties_list
     
    filters = []

    if neighborhood:
        filters.append(Properties.address_neighborhood.ilike(f"%{neighborhood}%"))

    if city:
        filters.append(Properties.address_city.ilike(f"%{city}%"))

    if state:
        filters.append(Properties.address_state.ilike(f"%{state}%"))

    if capacity:
        filters.append(Properties.capacity >= capacity)

    if price_max:
        filters.append(Properties.price_per_night <= price_max)

    if filters:
        properties_list = db.query(Properties).filter(*filters).all()
        return properties_list
    else:
        return({"message": "Nenhum filtro aplicado. Use 'list_all=True' para listar todas as propriedades."})
    
    