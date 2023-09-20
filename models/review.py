#!/usr/bin/python3
""" Review module for the HBNB project """
# Add base to the below import statement and to the review class inheritance
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id')
    user_id = Column(String(60), ForeignKey('users.id'))
    text = Column(String(1024), nullable=False)
