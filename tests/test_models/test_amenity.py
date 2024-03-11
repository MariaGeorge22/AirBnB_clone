#!/usr/bin/python3
""" Test file for Amenity Model """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Cases that will be tested for Amenity class """

    def setUp(self):
        """Set up the test environment"""
        self.amenity = Amenity()

    def test_amenity_is_a_subclass_of_base_model(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attr_is_a_class_attr(self):
        """Test if 'name' is a class attribute of Amenity"""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_class_attr(self):
        """Test properties of the 'name' class attribute"""
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))
