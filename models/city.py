#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, relationship

class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
    places = relationship(Place, cascade=delete, back_populates='cities')
