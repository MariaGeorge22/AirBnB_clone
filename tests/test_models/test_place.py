#!/usr/bin/python3
"""Test file for Place Model """
import unittest

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test cases for Place Class """
    def setUp(self):
        self.place = Place()
        self.attributes_list = ["name", "user_id", "city_id", "description",
                                "number_bathrooms", "max_guest",
                                "number_rooms", "price_by_night",
                                "latitude", "longitude", "amenity_ids"]

    def test_attributes_are_class_attributes(self):
        """
        Verifies that attributes in attributes_list are class attributes
        """
        for attribute in self.attributes_list:
            self.assertTrue(hasattr(Place, attribute))

    def test_class_attributes(self):
        """Checks the types and initial values of class attributes"""
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_bathrooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)

        for attribute in self.attributes_list:
            self.assertFalse(bool(getattr(self.place, attribute)))

    def test_accommodation_is_a_subclass_of_foundation_model(self):
        """Checks if Accommodation is a subclass of FoundationModel"""
        self.assertTrue(issubclass(type(self.place), BaseModel))
