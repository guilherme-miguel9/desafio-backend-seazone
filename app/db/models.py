from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Modelo da tabela de propriedades:
class Properties(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, index = True, nullable = False)
    address_street = Column(String, nullable = False)
    address_number = Column(Integer, nullable = False)
    address_neighborhood = Column(String, nullable = False)
    address_city = Column(String, nullable = False)
    address_state = Column(String, nullable = False)
    country = Column(String, nullable = False)
    rooms = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable = False)
    price_per_night = Column(Float, nullable = False)


