#!/usr/bin/env python3
"""Unittest amenity module.

Test cases for amenity class and methods documentation and instances.
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


class TestAmenity(unittest.TestCase):
    """Class for testing Amenity instances"""

    def setUp(self):
        """Initializes new Amenity instance for testing"""
        self.city = City()

    def test_instantiation(self):
        """... checks if Amenity is properly instantiated"""
        self.assertIsInstance(self.city, City)
