#!/usr/bin/python3
""" Base model """
import unittest
import os
import models
from models.base_model import BaseModel
from time import sleep
from datetime import datetime
from uuid import uuid4


class TestMyBaseModel(unittest.TestCase):
    """ base class """
    def test_instance_has_id(self):
        """
        Tests if an instance of BaseModel has the attribute 'id'.

        Raises:
            AssertionError: If the instance does not have the attribute 'id'.
        """
        my_instance = BaseModel()
        self.assertTrue(hasattr(my_instance, "id"))

    def test_string_representation(self):
        """
        Tests the string representation of BaseModel instances.

        Raises:
            AssertionError: If the string representation
            does not match the expected format.
        """
        my_instance = BaseModel()
        self.assertEqual(str(my_instance),
                         "[BaseModel] ({}) {}".format(my_instance.id,
                                                      my_instance.__dict__))

    def test_unique_ids_generation(self):
        """
        Check the valid ID

        Raises:
            AssertionError: If IDs generated for two instances are equal.
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_id_type_is_str(self):
        """
        chack if ID is STR

        Raises:
            AssertionError: If the ID type is not a string.
        """
        instance = BaseModel()
        self.assertTrue(type(instance.id) is str)

    def test_created_at_is_datetime_object(self):
        """
        Raises:
            AssertionError: If the 'created_at' attribute is not a datetime object.
        """
        instance = BaseModel()
        self.assertTrue(type(instance.created_at) is datetime)

    def test_updated_at_is_datetime_object(self):
        """
        Ensures that the 'updated_at' attribute is a datetime object.

        Raises:
            AssertionError: If the 'updated_at'
            attribute is not a datetime object.
        """
        instance = BaseModel()
        self.assertTrue(type(instance.updated_at) is datetime)

    def test_created_at_difference_between_two_models(self):
        """
        Tests if the 'created_at' attribute of one
        model instance is less than another.

        Raises:
            AssertionError: If the 'created_at' attribute
            of the first model is not less than the second model.
        """
        model1 = BaseModel()
        sleep(0.02)
        model2 = BaseModel()
        sleep(0.02)
        self.assertLess(model1.created_at, model2.created_at)

    def test_unused_args_attribute(self):
        """
        Tests if BaseModel instantiation with None argument
        doesn't result in None being in the instance attributes.

        Raises:
            AssertionError: If None is found in the instance attributes.
        """
        model = BaseModel(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_attributes(self):
        """
        Tests the existence of 'id', 'created_at', and 'updated_at'
        attributes in a BaseModel instance.

        Raises:
            AssertionError: If any of the attributes are missing.
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_save_method_updates_updated_at_attribute(self):
        """
        Tests if the 'save' method updates the 'updated_at' attribute.

        Raises:
            AssertionError: If 'updated_at' is not updated after calling 'save'
        """
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.created_at, model.updated_at)
        self.assertGreater(model.updated_at.microsecond,
                           model.created_at.microsecond)

    def test_to_dict_returns_dict_object(self):
        """
        Tests if the 'to_dict' method returns a dictionary object.

        Raises:
            AssertionError: If the returned value is not a dictionary.
        """
        model = BaseModel()
        self.assertTrue(type(model.to_dict()) is dict)

    def test_contains_class_dunder_method(self):
        """
        Raises:
            AssertionError: If '__class__' key is not found
            in the dictionary returned by to_dict().
        """
        model = BaseModel()
        self.assertTrue("__class__" in model.to_dict())

    def test_created_at_format_in_to_dict(self):
        """
        Raises:
            AssertionError: If the format of 'created_at'
            in the returned dictionary does not match the ISO format.
        """
        model = BaseModel()
        self.assertEqual(model.to_dict()["created_at"],
                         model.created_at.isoformat())

    def test_updated_at_format_in_to_dict(self):
        """
        Raises:
            AssertionError: If the format of 'updated_at'
            in the returned dictionary does not match the ISO format.
        """
        model = BaseModel()
        self.assertEqual(model.to_dict()["updated_at"],
                         model.updated_at.isoformat())

    def test_correct_number_of_keys_in_to_dict(self):
        """
        Raises:
            AssertionError: If the number of keys/values in the
            returned dictionary does not match the expected count.
        """
        model = BaseModel()
        expected_keys_count = len([key for key in model.__dict__
                                   if not key.startswith("_")]) + 1
        self.assertEqual(len(model.to_dict()), expected_keys_count)

    def test_generation_of_id_created_at_updated_at_when_kwargs_empty(self):
        """
        Raises:
            AssertionError: If any of 'id', 'created_at', or 'updated_at'
            are not generated automatically.
        """
        empty_dict = {}
        model = BaseModel(**empty_dict)
        self.assertTrue(type(model.id) is str)
        self.assertTrue(type(model.created_at) is datetime)
        self.assertTrue(type(model.updated_at) is datetime)

    def test_creation_from_kwargs(self):
        """
        Raises:
            AssertionError: If any of 'id', 'created_at', or
            'updated_at' are not assigned correctly.
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
        Raises:
            AssertionError: If BaseModel does not ignore args
            and sets the values from kwargs correctly.
        """
        current_datetime = datetime.now()
        dt_iso = current_datetime.isoformat()
        model = BaseModel("1234", id="234", created_at=dt_iso, name="Leah")
        self.assertEqual(model.id, "234")
        self.assertEqual(model.created_at, current_datetime)
        self.assertEqual(model.name, "Leah")

    def test_additional_kwargs_not_broken(self):
        """
        Raises:
            AssertionError: If BaseModel breaks or fails
            to handle additional attributes in kwargs.
        """
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "name": "Leah"}
        model = BaseModel(**my_dict)
        self.assertTrue(hasattr(model, "name"))

    def test_storage_new_not_called_with_dict_obj(self):
        """
        Raises:
            AssertionError: If storage.new() is called when
            BaseModel is created from a dict object.
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
        Raises:
            AssertionError: If save() method fails to
            update the 'updated_at' attribute.
        """
        model = BaseModel()
        sleep(0.02)
        temp_update = model.updated_at
        model.save()
        self.assertLess(temp_update, model.updated_at)

    def test_save_updates_twice(self):
        """
        Raises:
            AssertionError: If 'updated_at' is not
            updated twice by the save method.
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
        Raises:
            AssertionError: If the file is not updated when 'save' is called.
        """
        model = BaseModel()
        model.save()
        model_id = "BaseModel.{}".format(model.id)
        with open("file.json", encoding="utf-8") as f:
            self.assertIn(model_id, f.read())

    def test_correct_keys_in_to_dict(self):
        """
        Raises:
            AssertionError: If to_dict() does not return the expected keys.
        """
        model_dict = BaseModel().to_dict()
        expected_keys = ("id", "created_at", "updated_at", "__class__")
        for key in expected_keys:
            self.assertIn(key, model_dict)

    def test_additional_attributes_in_to_dict(self):
        """
        Raises:
            AssertionError: If new attributes are not returned by to_dict().
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
        Raises:
            AssertionError: If the output returned by to_dict()
            does not match the expected output.
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
        Raises:
            AssertionError: If TypeError is not raised
            when an argument is passed to to_dict().
        """
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.to_dict(None)

    def test_to_dict_not_equal_to_dunder_dict(self):
        model = BaseModel()
        self.assertNotEqual(model.to_dict(), model.__dict__)


if __name__ == "__main__":
    unittest.main()
