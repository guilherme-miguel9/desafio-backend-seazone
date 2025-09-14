from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
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


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey("properties.id"), nullable=False)
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    guests_quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)

