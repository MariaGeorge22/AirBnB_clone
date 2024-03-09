#!/usr/bin/python3
"""Test file for City Model """
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Test cases for City Class """

    def setUp(self):
        """
        Initializes necessary objects before each test
        """
        self.urban_area = City()
        self.attribute_list = ["state_id", "name"]

    def test_urban_area_is_a_derived_class_of_foundation_model(self):
        """
        Checks if UrbanArea is a subclass of FoundationModel
        """
        self.assertTrue(issubclass(type(self.urban_area), BaseModel))

    def test_attributes_are_class_attributes(self):
        """
        Verifies that attributes are class attributes
        """
        for attribute in self.attribute_list:
            self.assertIs(type(getattr(self.urban_area, attribute)), str)
            self.assertFalse(bool(getattr(self.urban_area, attribute)))
