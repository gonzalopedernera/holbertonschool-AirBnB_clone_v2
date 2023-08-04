#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models.amenity import Amenity
import os


class TestAmenity(unittest.TestCase):
    """ Tests for Amenity Class"""

    def tearDown(self) -> None:
        """ teardown method """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_create_class(self):
        """ Tests if the class was created correctly """
        a1 = Amenity()
        self.assertIsInstance(a1, Amenity)
        self.assertTrue(hasattr(a1, "name"))

    def test_empty_attributes(self):
        """ Tests if the atribute its empty """
        a1 = Amenity()
        self.assertAlmostEqual(a1.name, "")


if __name__ == "__main__":
    unittest.main()
