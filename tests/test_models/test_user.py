#!/usr/bin/python3
""" The User Model """

from models import storage
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import unittest


class TestUser(unittest.TestCase):

    """ Cases of User Class """

    def setUp(self):
        """Sets up the environment for testing."""
        # Describes the action of initializing the testing environment.
        pass

    def clean_up_test_environment(self):
        """Performs cleanup after testing."""
        # Describes the action of cleaning up after testing.
        self.resetStorage()
        pass

    def reset_storage(self):
        """Clears data stored in the storage."""
        # Describes the action of resetting the storage.
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance_creation(self):
        """Tests the creation of instances of the User."""
        # Describes the purpose of testing instance creation of User.
        instance = User()
        self.assertEqual(str(type(instance)), "<class 'models.user.User'>")
        self.assertIsInstance(instance, User)
        self.assertTrue(issubclass(type(instance), BaseModel))

    def test_attribute_verification(self):
        """Verifies the attributes of the CustomClass."""
        # Describes thePurpose oftesting attribute verification of CustomClass
        attributes = storage.attributes()["User"]
        obj = User()
        for key, value in attributes.items():
            self.assertTrue(hasattr(obj, key))
            self.assertEqual(type(getattr(obj, key, None)), value)


if __name__ == "__main__":
    unittest.main()
