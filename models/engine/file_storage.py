#!/usr/bin/env python3
"""FileStorage Class.

This module contains a class that serializes instances to a JSON file
and deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Defines the blueprint of saving and retrieving objects .

    Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets object with key <obj class name>.id in objects dictionary"""
        class_name = type(obj).__name__
        obj_id = obj.id
        key = "{}.{}".format(class_name, obj_id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects to the JSON file"""
        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objects_loaded = json.load(f)

                new_dict = {}
                for obj_name, obj_details in objects_loaded.items():
                    obj = BaseModel(**obj_details)
                    new_dict[obj_name] = obj

                FileStorage.__objects = new_dict
        except:
            pass
