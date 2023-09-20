#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
            primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
            primary_key=True, nullable=False)
        )

class Place(BaseModel):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    amenity_ids = []

    storage = getenv('HBNB_TYPE_STORAGE', None)
    if storage != 'db':
        def amenities(self):
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

         def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)

         def reviews(self, place_id):
        """"Returns a list of reviews"""
        from models.review import Review

        all_reviews = self.all(Review)
        reviews_list = []
        for review in all_reviews.values():
            if review.place_id == place_id:
                reviews_list.append(review)
        return reviews_list
