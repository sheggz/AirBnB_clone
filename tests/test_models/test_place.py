#!/usr/bin/env python3
"""Unittest place module.

Test cases for place class and methods documentation and instances.
"""
import unittest

from models import place


Place = place.Place


class TestPlaceDocs(unittest.TestCase):
    """Class for testing place docs"""

    def test_doc_file(self):
        """... documentation for the file"""
        doc = place.__doc__
        self.assertIsNotNone(doc)

    def test_doc_class(self):
        """... documentation for the class"""
        doc = Place.__doc__
        self.assertIsNotNone(doc)


class TestPlace(unittest.TestCase):
    """Class for testing Place instances"""

    def setUp(self):
        """Initializes new Place instance for testing"""
        self.place = Place()

    def test_instantiation(self):
        """... checks if Place is properly instantiated"""
        self.assertIsInstance(self.place, Place)
