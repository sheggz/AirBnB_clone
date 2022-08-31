#!/usr/bin/env python3
"""Unittest base_model module.

Test cases for base_model class and methods documentation and instances.
"""
import unittest

from datetime import datetime
from models import base_model


BaseModel = base_model.BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    def test_doc_file(self):
        """... documentation for the file"""
        doc = base_model.__doc__
        self.assertIsNotNone(doc)

    def test_doc_class(self):
        """... documentation for the class"""
        doc = BaseModel.__doc__
        self.assertIsNotNone(doc)

    def test_doc_init(self):
        """... documentation for init function"""
        doc = BaseModel.__init__.__doc__
        self.assertIsNotNone(doc)

    def test_doc_save(self):
        """... documentation for save function"""
        doc = BaseModel.save.__doc__
        self.assertIsNotNone(doc)

    def test_doc_to_dict(self):
        """... documentation for to_dict function"""
        doc = BaseModel.to_dict.__doc__
        self.assertIsNotNone(doc)

    def test_doc_str(self):
        """... documentation for to str function"""
        doc = BaseModel.__str__.__doc__
        self.assertIsNotNone(doc)


class TestBaseModel(unittest.TestCase):
    """Class for testing BaseModel instances"""

    def setUp(self):
        """Initializes new BaseModel instance for testing"""
        self.model = BaseModel()

    def test_instantiation(self):
        """... checks if BaseModel is properly instantiated"""
        self.assertIsInstance(self.model, BaseModel)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.model)
        my_list = ["BaseModel", "id", "created_at"]
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_save(self):
        """... save function should update updated_at attribute"""
        self.model.save()
        actual = self.model.created_at
        expected = datetime.now()
        self.assertNotEqual(expected, actual)

    def test_to_dict(self):
        """... checks if BaseModel is properly casted to dictionary"""
        my_model = self.model.to_dict()
        if "__class__" in my_model:
            self.assertEqual(my_model["__class__"], "BaseModel")
        for key in ("created_at", "updated_at"):
            self.assertIsInstance(my_model[key], str)
