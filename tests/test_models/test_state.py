#!/usr/bin/python3
"""
Unittest for State class
"""
import unittest
from models.state import State
import os


class TestState(unittest.TestCase):
    """ Tests for State Class"""

    def tearDown(self) -> None:
        """ teardown method """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_create_class(self):
        """ Tests if the class was created correctly """
        u1 = State()
        self.assertIsInstance(u1, State)
        self.assertTrue(hasattr(u1, "name"))

    def test_empty_attributes(self):
        """ Tests if the atribute its empty """
        u1 = State()
        self.assertAlmostEqual(u1.name, "")


if __name__ == "__main__":
    unittest.main()
