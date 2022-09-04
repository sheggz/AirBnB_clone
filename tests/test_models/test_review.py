#!/usr/bin/env python3
"""Unittest review module.

Test cases for review class and methods documentation and instances.
"""
import unittest

from models import review


Review = review.Review


class TestReviewDocs(unittest.TestCase):
    """Class for testing review docs"""

    def test_doc_file(self):
        """... documentation for the file"""
        doc = review.__doc__
        self.assertIsNotNone(doc)

    def test_doc_class(self):
        """... documentation for the class"""
        doc = Review.__doc__
        self.assertIsNotNone(doc)


class TestReview(unittest.TestCase):
    """Class for testing Place instances"""

    def setUp(self):
        """Initializes new Review instance for testing"""
        self.review = Review()

    def test_instantiation(self):
        """... checks if Review is properly instantiated"""
        self.assertIsInstance(self.review, Review)
