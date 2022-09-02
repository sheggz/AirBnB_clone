#!/usr/bin/python3
"""BaseModel Class.

This module contains a class that defines all other classes in this project.
"""
import models
import uuid
from datetime import datetime


time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Defines the blueprint of the subclasses.

    Attributes:
        id: string - assign with an uuid when an object is created
        created_at: datetime - assign with the current datetime when an
                    object is created
        updated_at: datetime - assign with the current datetime when an
                    object is created and it will be updated every time
                    you change your object
    """

    def __init__(self, *args, **kwargs):
        """An object constructor method"""
        if kwargs:
            self.__dict__ = kwargs
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs.get("created_at"),
                                                    time_format)
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs.get("updated_at"),
                                                    time_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """A string representation of object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
