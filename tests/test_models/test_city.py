#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
from models.city import City
import os


class TestCity(unittest.TestCase):
    """ Tests for City Class"""

    def tearDown(self) -> None:
        """ teardown method """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_create_class(self):
        """ Tests if the class was created correctly """
        c1 = City()
        self.assertIsInstance(c1, City)
        self.assertTrue(hasattr(c1, "state_id"))
        self.assertTrue(hasattr(c1, "name"))

    def test_empty_attributes(self):
        """ Tests if the atribute its empty """
        c1 = City()
        self.assertAlmostEqual(c1.state_id, "")
        self.assertAlmostEqual(c1.name, "")


if __name__ == "__main__":
    unittest.main()
