#!/usr/bin/python3
"""file storage test cases """
import os.path
import unittest

import models
from models import base_model
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


class TestFileStorageInit(unittest.TestCase):
    """FileStorage class """

    def test_file_path_is_a_private_class_attr(self):
        """
        Checks that file_path is a private class attribute.

        It verifies that the FileStorage class does not
        expose the file_path attribute.
        """
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_objects_is_a_private_class_attr(self):
        """
        Checks that objects is a private class attribute.

        It verifies that the FileStorage class does not
        expose the __objects attribute.
        """
        self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_init_without_arg(self):
        """
        Tests initialization without arguments.

        It verifies that FileStorage can be
        instantiated without arguments.
        """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_init_with_arg(self):
        """
        Tests initialization with arguments.

        It verifies that FileStorage raises a TypeError
        when instantiated with arguments.
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialization(self):
        """
        Tests the storage initialization created in __init__.py.

        It ensures that the storage instance created
        in __init__.py is of type FileStorage.
        """
        self.assertEqual(type(models.storage), FileStorage)


class TestStorageMethods(unittest.TestCase):
    """ FileStorage against """

    @classmethod
    def setUp(self):
        """Code to execute before testing occurs"""
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """
        Code to execute after tests are executed.

        This method is called after each test method
        and performs cleanup operations.
        """
        # Remove file.json if it exists
        try:
            os.remove("file.json")
        except IOError:
            pass

        # rename tmp.json from setUp() to file.json
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """
        Tests the all() method of the FileStorage class.

        Checks if the all() method returns a dictionary
        containing all objects
        stored in the FileStorage instance.

        Raises:
            AssertionError: If the method does not return
            a dictionary or if an
            argument is passed, which should raise a TypeError
        """
        self.assertTrue(type(models.storage.all()) is dict)

        # If an arg is passed, TypeError is raised
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_method(self):
        """
        Tests the new() method of the FileStorage class.

        Creates instances of all supported classes and checks if the new()
        method correctly adds them to the storage.

        Raises:
            AssertionError: If an instance is not added to the storage, if more
                             than one argument is passed, or if None is passed,
                             which should raise TypeError and AttributeError
                             respectively.
        """
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        # Checks that the objects created above are stored
        self.assertIn("BaseModel." + dummy_bm.id,
                      models.storage.all().keys())
        self.assertIn(dummy_bm, models.storage.all().values())
        self.assertIn("User." + dummy_user.id, models.storage.all().keys())
        self.assertIn(dummy_user, models.storage.all().values())
        self.assertIn("State." + dummy_state.id, models.storage.all().keys())
        self.assertIn(dummy_state, models.storage.all().values())
        self.assertIn("Place." + dummy_place.id, models.storage.all().keys())
        self.assertIn(dummy_place, models.storage.all().values())
        self.assertIn("City." + dummy_city.id, models.storage.all().keys())
        self.assertIn(dummy_city, models.storage.all().values())
        self.assertIn("Amenity." + dummy_amenity.id,
                      models.storage.all().keys())
        self.assertIn(dummy_amenity, models.storage.all().values())
        self.assertIn("Review." + dummy_review.id,
                      models.storage.all().keys())
        self.assertIn(dummy_review, models.storage.all().values())

        # If more than one arg is passed, TypeError is raised
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

        # If None is passed, then AttributeError is raised
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_method(self):
        """
        Tests the save() method of the FileStorage class.

        Creates instances of all supported classes, saves them using the
        save() method, and checks if they are correctly stored in the file.

        Raises:
            AssertionError: If instances are not
            correctly saved in the file or
            if an argument is passed, which should raise a TypeError.
        """
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        models.storage.save()

        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + dummy_bm.id, save_text)
            self.assertIn("User." + dummy_user.id, save_text)
            self.assertIn("State." + dummy_state.id, save_text)
            self.assertIn("Place." + dummy_place.id, save_text)
            self.assertIn("City." + dummy_city.id, save_text)
            self.assertIn("Amenity." + dummy_amenity.id, save_text)
            self.assertIn("Review." + dummy_review.id, save_text)

        # When an arg is passed, TypeError is raised
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_method(self):
        """
        Tests the reload method of the FileStorage class.

        Saves the current state of the storage, reloads it using the reload()
        method, and checks if the objects are correctly
        loaded back into the storage.

        Raises:
            AssertionError: If objects are not correctly
            reloaded into the storage
            or if an argument is passed, which should raise a TypeError.
        """
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + dummy_bm.id, objects)
        self.assertIn("User." + dummy_user.id, objects)
        self.assertIn("State." + dummy_state.id, objects)
        self.assertIn("Place." + dummy_place.id, objects)
        self.assertIn("City." + dummy_city.id, objects)
        self.assertIn("Amenity." + dummy_amenity.id, objects)
        self.assertIn("Review." + dummy_review.id, objects)

        # If an arg is passed, then TypeError is raised
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
