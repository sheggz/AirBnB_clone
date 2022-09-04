#!/usr/bin/env python3
"""Unittest user module.

Test cases for user class and methods documentation and instances.
"""
import unittest

from models import user


User = user.User


class TestUserDocs(unittest.TestCase):
    """Class for testing user docs"""

    def test_doc_file(self):
        """... documentation for the file"""
        doc = user.__doc__
        self.assertIsNotNone(doc)

    def test_doc_class(self):
        """... documentation for the class"""
        doc = User.__doc__
        self.assertIsNotNone(doc)


class TestUser(unittest.TestCase):
    """Class for testing User instances"""

    def setUp(self):
        """Initializes new User instance for testing"""
        self.user = User()

    def test_instantiation(self):
        """... checks if User is properly instantiated"""
        self.assertIsInstance(self.user, User)
