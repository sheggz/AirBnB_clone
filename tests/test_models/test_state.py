#!/usr/bin/env python3
"""Unittest state module.

Test cases for state class and methods documentation and instances.
"""
import unittest

from models import state


State = state.State


class TestStateDocs(unittest.TestCase):
    """Class for testing state docs"""

    def test_doc_file(self):
        """... documentation for the file"""
        doc = state.__doc__
        self.assertIsNotNone(doc)

    def test_doc_class(self):
        """... documentation for the class"""
        doc = State.__doc__
        self.assertIsNotNone(doc)


class TestState(unittest.TestCase):
    """Class for testing State instances"""

    def setUp(self):
        """Initializes new State instance for testing"""
        self.state = State()

    def test_instantiation(self):
        """... checks if State is properly instantiated"""
        self.assertIsInstance(self.state, State)
