#!/usr/bin/python3
""" Test file for Amenity Model """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Cases that will be tested for Amenity class """

    def setUp(self):
        """Set up the test environment"""
        # Creating an instance of AmenityClass for testing
        self.amenity = Amenity()

    def test_amenity_is_a_subclass_of_base_model(self):
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def TestClassAttr(self):
        """Test the properties of the 'name' class attribute"""
        # Checking the type and initial value of the 'name' attribute
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))

    def TestAttr_isA_ClassAttr(self):
        """Test if 'name' is a class attribute of AmenityClass"""
        # Checking if 'name' is a class attribute of AmenityClass
        self.assertTrue(hasattr(self.amenity, "name"))
