#!/usr/bin/python3
"""BaseModel Class.

This module contains a class that defines all other classes in this project.
"""
import uuid
from datetime import datetime


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

    def __init__(self):
        """An object constructor method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """A string representation of object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
