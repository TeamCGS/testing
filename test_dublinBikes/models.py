from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Static(Base):
    __tablename__ = 'Stations'
    
    number = Column(Integer, primary_key=True, nullable=False)
    name = Column(String (100), nullable=False)
    address = Column(String (100), nullable=False)
    location_latitude = Column(Float, nullable=False)
    location_longitude = Column(Float, nullable=False)
    banking = Column(Boolean, nullable=False)
    bonus = Column(Boolean, nullable=False)
    
    def __init__(self, number=None, name=None, address=None, location_latitude=None, location_longitude=None, banking=None, bonus=None):
        self.number = number
        self.name = name
        self.address = address
        self.location_latitude = location_latitude
        self.location_longitude = location_longitude
        self. banking = banking
        self.bonus = bonus

    def __repr__(self):
        return '<Station %r>' % (self.name)
    