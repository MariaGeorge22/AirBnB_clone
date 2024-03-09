#!/usr/bin/python3
"""Test file for Review Model """
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ Test cases for Review Class """
    def setUp(self):
        """
        Initializes necessary objects before each test
        """
        self.review = Review()
        self.attributes_list = [
            "place_id",
            "user_id",
            "text"
        ]

    def test_reviewIsA_subclassOf_base_model(self):
        """
        Verifies that Review is a subclass of BaseModel
        """
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_class_attributes(self):
        """
        Checks the types and initial values of class attributes
        """
        for attribute in self.attributes_list:
            self.assertIs(type(getattr(self.review, attribute)), str)
            self.assertFalse(bool(getattr(self.review, attribute)))

    def test_attributes_are_class_attributes(self):
        """
        Verifies that attributes in attributes_list are class attributes
        """
        for attribute in self.attributes_list:
            self.assertTrue(hasattr(self.review, attribute))
