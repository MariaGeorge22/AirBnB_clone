#!/usr/bin/python3
"""Test file for User Model """
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ Test cases for User Class """
    def test_attributes_are_class_attributes(self):
        """
        Verifies that first_name and last_name are class attributes
        """
        user = User()
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))

    def test_user_is_a_subclass_of_base_model(self):
        """
        Verifies that User is a subclass of BaseModel
        """
        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_class_attributes(self):
        """
        Checks the types and initial values of class attributes
        """
        user = User()
        self.assertIs(type(user.first_name), str)
        self.assertIs(type(user.last_name), str)
        self.assertTrue(user.first_name == "")
        self.assertTrue(user.last_name == "")
