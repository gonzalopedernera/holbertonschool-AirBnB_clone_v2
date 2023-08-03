#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import os
from models.user import User


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenities,
        back_populates='places',
        viewonly=False)
    else:
        @property
        def reviews(self):
            from models import storage
            reviews = []
            for key, value in storage.__objects.items():
                splited_key = key.split('.')
                if splited_key[0] == 'Review':
                    reviews.append(value)
            filtered_reviews = list(
                filter(lambda x: x.place_id == self.id), reviews)
            return filtered_reviews
        
        @property
        def amenities(self):
            from models import storage
            amenities = []
            for key, value in storage.__objects.items():
                splited_key = key.split('.')
                if splited_key[0] == 'Amenity':
                    amenities.append(value)
            self.amenity_ids = list(
                filter(lambda x: x.place_id == self.id), amenities)
            return self.amenity_ids
        
        @amenities.setter
        def amenities(self, obj):
            if obj.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)


