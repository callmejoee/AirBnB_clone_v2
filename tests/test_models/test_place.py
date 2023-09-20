#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.base_model import BaseModel


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        self.assertIsInstance(Place.city_id, str)
        self.assertTrue(issubclass(Place, BaseModel))

    def test_user_id(self):
        """ """
        self.assertIsInstance(Place.user_id, str)

    def test_name(self):
        """ """
        self.assertIsInstance(Place.name, str)

    def test_description(self):
        """ """
        self.assertIsInstance(Place.description, str)

    def test_number_rooms(self):
        """ """
        self.assertIsInstance(Place.number_rooms, int)

    def test_number_bathrooms(self):
        """ """
        self.assertIsInstance(Place.number_bathrooms, int)

    def test_max_guest(self):
        """ """
        self.assertIsInstance(Place.max_guest, int)

    def test_price_by_night(self):
        """ """
        self.assertIsInstance(Place.price_by_night, int)

    def test_latitude(self):
        """ """
        self.assertIsInstance(Place.latitude, float)

    def test_longitude(self):
        """ """
        self.assertIsInstance(Place.latitude, float)

    def test_amenity_ids(self):
        """ """
        self.assertIsInstance(Place.amenity_ids, list)
