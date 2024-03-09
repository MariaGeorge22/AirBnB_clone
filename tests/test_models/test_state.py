#!/usr/bin/python3
"""Test file for State Model """
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Test cases for State Class """
    def setUp(self):
        self.state = State()

    def test_custom_entity_is_a_subclass_of_model_base(self):
        """
        Verifies that the custom entity is a subclass of ModelBase
        """
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_class_attributes(self):
        """
        Checks the type and initial value of the class attribute "name"
        """
        self.assertIs(type(self.state.name), str)
        self.assertFalse(bool(self.state.name))

    def test_attribute_is_a_class_attribute(self):
        """
        Verifies that the attribute "name" is a class attribute
        """
        self.assertTrue(hasattr(self.state, "name"))
