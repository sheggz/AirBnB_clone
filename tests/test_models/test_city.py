#!/usr/bin/env python3
"""Unittest city module.

Test cases for city class and methods documentation and instances.
"""
import unittest

from models import city


City = city.City


class TestCityDocs(unittest.TestCase):
    """Class for testing City docs"""

    def test_doc_file(self):
        """... documentation for the file"""
        doc = city.__doc__
        self.assertIsNotNone(doc)

    def test_doc_class(self):
        """... documentation for the class"""
        doc = City.__doc__
        self.assertIsNotNone(doc)


class TestCity(unittest.TestCase):
    """Class for testing City instances"""

    def setUp(self):
        """Initializes new City instance for testing"""
        self.city = City()

    def test_instantiation(self):
        """... checks if City is properly instantiated"""
        self.assertIsInstance(self.city, City)
