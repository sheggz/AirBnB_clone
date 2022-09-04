#!/usr/bin/env python3
"""Unittest console module.

Test cases for console class and methods documentation and instances.
"""
import console
import unittest


HBNBCommand = console.HBNBCommand


class TestHBNBCommandDocs(unittest.TestCase):
    """Class for testing console docs"""

    def test_doc_file(self):
        """... documentation for the file"""
        doc = console.__doc__
        self.assertIsNotNone(doc)

    def test_doc_class(self):
        """... documentation for the class"""
        doc = HBNBCommand.__doc__
        self.assertIsNotNone(doc)


if __name__ == '__main__':
    unittest.main
