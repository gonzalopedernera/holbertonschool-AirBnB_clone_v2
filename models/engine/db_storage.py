#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.state import State
import os


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        from models.base_model import Base
        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        if host == 'here':
            host = 'localhost'
        db_name = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            username,
            password,
            host,
            db_name
        ), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.user import User
        from models.base_model import BaseModel
        classes = {"User": User, "BaseModel": BaseModel, "Place": Place,
                   "State": State, "City": City, "Amenity": Amenity,
                   "Review": Review}

        objects = {}
        if cls != '':
            for instance in self.__session.query(cls):
                instance_key = instance.__class__.__name__ + '.' + instance.id
                objects[instance_key] = instance
            return objects
        else:
            for key, value in classes.items():
                if key != "BaseModel":
                    all_objs = self.__session.query(value).all()
                    if len(all_objs) > 0:
                        for ins in all_objs:
                            k = ins.__class__.__name__ + '.' + ins.id
                            objects[k] = ins
            return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        from models.base_model import Base
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.user import User

        Base.metadata.create_all(self.__engine)
        session_creation = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_creation)
        self.__session = Session()

    def close(self):
        """Closes the current session"""
        self.__session.close()
