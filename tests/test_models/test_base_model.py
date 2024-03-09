#!/usr/bin/python3
"""
Test suite for the BaseModel class in the models module
"""
import unittest
import os
import models
from models.base_model import BaseModel
from time import sleep
from datetime import datetime
from uuid import uuid4


class TestMyBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """
    def test_instance_has_id(self):
        my_instance = BaseModel()
        self.assertTrue(hasattr(my_instance, "id"))

    def test_string_representation(self):
        my_instance = BaseModel()
        self.assertEqual(str(my_instance),
                         "[BaseModel] ({}) {}".format(my_instance.id,
                                                      my_instance.__dict__))

    def test_unique_ids_generation(self):
        """
        Validates if IDs are generated randomly and are unique
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_id_type_is_str(self):
        """
        Verifies that the generated ID is of string type
        """
        instance = BaseModel()
        self.assertTrue(type(instance.id) is str)

    def test_created_at_is_datetime_object(self):
        """
        Ensures that the 'created_at' attribute is a datetime object
        """
        instance = BaseModel()
        self.assertTrue(type(instance.created_at) is datetime)

    def test_updated_at_is_datetime_object(self):
        instance = BaseModel()
        self.assertTrue(type(instance.updated_at) is datetime)

    def test_created_at_difference_between_two_models(self):
        model1 = BaseModel()
        sleep(0.02)
        model2 = BaseModel()
        sleep(0.02)
        self.assertLess(model1.created_at, model2.created_at)

    def test_unused_args_attribute(self):
        model = BaseModel(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_created_at_equals_updated_at_initially(self):
        model = BaseModel()
        self.assertEqual(model.created_at, model.updated_at)

    def test_save_method_updates_updated_at_attribute(self):
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.created_at, model.updated_at)
        self.assertGreater(model.updated_at.microsecond,
                           model.created_at.microsecond)

    def test_to_dict_returns_dict_object(self):
        model = BaseModel()
        self.assertTrue(type(model.to_dict()) is dict)

    def test_contains_class_dunder_method(self):
        """
        Validates if BaseModel's to_dict() method contains the key '__class__'
        """
        model = BaseModel()
        self.assertTrue("__class__" in model.to_dict())

    def test_created_at_format_in_to_dict(self):
        """
        Verifies that 'created_at' is stored in ISO format
        as a string in BaseModel's to_dict()
        """
        model = BaseModel()
        self.assertEqual(model.to_dict()["created_at"],
                         model.created_at.isoformat())

    def test_updated_at_format_in_to_dict(self):
        """
        Verifies that 'updated_at' is stored in ISO format
        as a string in BaseModel's to_dict()
        """
        model = BaseModel()
        self.assertEqual(model.to_dict()["updated_at"],
                         model.updated_at.isoformat())

    def test_correct_number_of_keys_in_to_dict(self):
        """
        Ensures that to_dict() returns the expected number of keys/values
        """
        model = BaseModel()
        expected_keys_count = len([key for key in model.__dict__
                                   if not key.startswith("_")]) + 1
        self.assertEqual(len(model.to_dict()), expected_keys_count)

    def test_generation_of_id_created_at_updated_at_when_kwargs_empty(self):
        """
        Validates that 'id', 'created_at', and 'updated_at' are automatically
        generated if they're not passed in kwargs
        """
        empty_dict = {}
        model = BaseModel(**empty_dict)
        self.assertTrue(type(model.id) is str)
        self.assertTrue(type(model.created_at) is datetime)
        self.assertTrue(type(model.updated_at) is datetime)

    def test_creation_from_kwargs(self):
        """
        Ensures that 'id', 'created_at', and 'updated_at'
        are correctly assigned when provided in kwargs
        """
        my_kwargs = {"id": uuid4(),
                     "created_at": datetime.utcnow().isoformat(),
                     "updated_at": datetime.utcnow().isoformat()}
        model = BaseModel(**my_kwargs)
        self.assertEqual(model.id, my_kwargs["id"])
        self.assertEqual(model.created_at,
                         datetime.strptime(my_kwargs["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(model.updated_at,
                         datetime.strptime(my_kwargs["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

    def test_kwargs_over_args(self):
        """
        Validates that when both args and kwargs are passed,
        BaseModel ignores args
        """
        current_datetime = datetime.now()
        dt_iso = current_datetime.isoformat()
        model = BaseModel("1234", id="234", created_at=dt_iso, name="Leah")
        self.assertEqual(model.id, "234")
        self.assertEqual(model.created_at, current_datetime)
        self.assertEqual(model.name, "Leah")

    def test_additional_kwargs_not_broken(self):
        """
        Ensures BaseModel does not break when kwargs
        contain additional attributes
        """
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "name": "Leah"}
        model = BaseModel(**my_dict)
        self.assertTrue(hasattr(model, "name"))

    def test_storage_new_not_called_with_dict_obj(self):
        """
        Verifies that storage.new() is not called
        when BaseModel is created from a dict object
        """
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "name": "Leah"}
        model = BaseModel(**my_dict)
        self.assertTrue(model not in models.storage.all().values())
        del model

        model = BaseModel()
        self.assertTrue(model in models.storage.all().values())

    def test_save_updates_updated_at_attribute(self):
        """
        Checks that save() method updates the 'updated_at' attribute
        """
        model = BaseModel()
        sleep(0.02)
        temp_update = model.updated_at
        model.save()
        self.assertLess(temp_update, model.updated_at)

    def test_save_updates_twice(self):
        """
        Tests that the save method updates 'updated_at' two times
        """
        model = BaseModel()
        sleep(0.02)
        temp_update = model.updated_at
        model.save()
        sleep(0.02)
        temp1_update = model.updated_at
        self.assertLess(temp_update, temp1_update)
        sleep(0.01)
        model.save()
        self.assertLess(temp1_update, model.updated_at)

    def test_save_updates_file(self):
        """
        Tests if the file is updated when 'save' is called
        """
        model = BaseModel()
        model.save()
        model_id = "BaseModel.{}".format(model.id)
        with open("file.json", encoding="utf-8") as f:
            self.assertIn(model_id, f.read())

    def test_correct_keys_in_to_dict(self):
        """
        Verifies that to_dict() returns the expected keys
        """
        model_dict = BaseModel().to_dict()
        expected_keys = ("id", "created_at", "updated_at", "__class__")
        for key in expected_keys:
            self.assertIn(key, model_dict)

    def test_additional_attributes_in_to_dict(self):
        """
        Checks that new attributes are also returned by to_dict()
        """
        model = BaseModel()
        model.name = "Leah"
        model.email = "leahk@gmail.com"
        expected_attributes = ["id", "created_at",
                               "updated_at", "__class__", "name", "email"]
        for attr in expected_attributes:
            self.assertIn(attr, model.to_dict())

    def test_to_dict_output(self):
        """
        Verifies the output returned by to_dict()
        """
        model = BaseModel()
        current_datetime = datetime.now()
        model.id = "12345"
        model.created_at = model.updated_at = current_datetime
        expected_dict = {
            'id': "12345",
            'created_at': current_datetime.isoformat(),
            'updated_at': current_datetime.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(expected_dict, model.to_dict())

    def test_to_dict_with_args_raises_type_error(self):
        """
        Checks that TypeError is raised when an argument is passed to to_dict()
        """
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.to_dict(None)

    def test_to_dict_not_equal_to_dunder_dict(self):
        """
        Verifies that to_dict() is a dictionary object
        and not equal to __dict__
        """
        model = BaseModel()
        self.assertNotEqual(model.to_dict(), model.__dict__)


if __name__ == "__main__":
    unittest.main()
