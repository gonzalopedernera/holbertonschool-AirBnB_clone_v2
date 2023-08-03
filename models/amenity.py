#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = Table('place_amenity', metadata=Base.metadata,
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    amenity_id = Column(String(60), ForeignKey('amenities.id'), nullable=False)
    )
