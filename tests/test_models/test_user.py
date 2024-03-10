#!/usr/bin/python3
""" User Model """

import unittest
from models.user import User
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """User Class"""

    def setUp(self):
        """
        Sets up the test environment before each test method is executed.
        This method is called automatically by the testing framework.
        """
        pass

    def tearDown(self):
        """
        Cleans up the test environment after each test method is executed.
        This method is called automatically by the testing framework.
        """
        self.resetStorage()
        pass

    def resetStorage(self):
        """
        Resets the FileStorage data to its initial state.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """
        Tests the instantiation of the User class.

        It checks if an instance of the User class is created correctly
        and if it inherits from BaseModel.
        """

        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """
        Tests the attributes of the User class.

        It verifies if all attributes specified in the storage are
        present in an instance of the User class.
        """
        attributes = storage.attributes()["User"]
        obj = User()
        for key, value in attributes.items():
            self.assertTrue(hasattr(obj, key))
            self.assertEqual(type(getattr(obj, key, None)), value)


if __name__ == "__main__":
    unittest.main()
