#!/usr/bin/python3
"""Module for the Foundation Class
Incorporates the Foundation class for the AirBnB emulation console.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """Class representing the fundamental model in the object hierarchy."""

    def __init__(self, *args, **kwargs):
        """Initializing a Base instance.
            Parameters:
                - *args: list of arguments
                - **kwargs: dictionary of key-value arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Provides a human-readable string representation
            of an instance."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Produces a dictionary representation containing
            detailed information of an instance."""

        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
