#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import storage
from models.city import City
from models import HBNB_TYPE_STORAGE


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if HBNB_TYPE_STORAGE == 'db':
        cities = relationship("City", cascade='all, delete', backref='state')

    @property
    def cities(self):
        '''getter attribute cities that returns the list of City
        instances with state_id equals to the current State.id'''
        cits_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cits_list.append(city)
        return cits_list
