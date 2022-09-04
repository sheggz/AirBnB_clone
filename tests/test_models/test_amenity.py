#!/usr/bin/env python3
"""Unittest amenity module.

Test cases for amenity class and methods documentation and instances.
"""
import unittest

from models import amenity


Amenity = amenity.Amenity


class TestAmenityDocs(unittest.TestCase):
    """Class for testing Amenity docs"""

    def test_doc_file(self):
        """... documentation for the file"""
        doc = amenity.__doc__
        self.assertIsNotNone(doc)

    def test_doc_class(self):
        """... documentation for the class"""
        doc = Amenity.__doc__
        self.assertIsNotNone(doc)


class TestAmenity(unittest.TestCase):
    """Class for testing Amenity instances"""

    def setUp(self):
        """Initializes new Amenity instance for testing"""
        self.amenity = Amenity()

    def test_instantiation(self):
        """... checks if Amenity is properly instantiated"""
        self.assertIsInstance(self.amenity, Amenity)
