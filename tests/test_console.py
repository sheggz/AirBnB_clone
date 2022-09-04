#!/usr/bin/env python3
"""Unittest console module.

Test cases for console class and methods documentation and instances.
"""
import unittest

import console


Console = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing console docs"""

    def test_doc_file(self):
        """... documentation for the file"""
        doc = console.__doc__
        self.assertIsNotNone(doc)

    def test_doc_class(self):
        """... documentation for the class"""
        doc = Console.__doc__
        self.assertIsNotNone(doc)


class TestConsole(unittest.TestCase):
    """Class for testing Console instances"""
