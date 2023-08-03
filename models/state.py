#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.engine.db_storage import DBStorage
        cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            from models import storage
            cities = []
            for key, value in storage.__objects.items():
                l = key.split('.')
                if l[0] == 'City':
                    cities.append(value)
            filtered_cities = list(filter(lambda x: x.state_id == self.id), cities)
            return filtered_cities


