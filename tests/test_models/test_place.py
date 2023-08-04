#!/usr/bin/python3
"""
Unittest for Place class
"""
import unittest
from models.place import Place
import os


class TestPlace(unittest.TestCase):
    """ Tests for Place Class"""

    def tearDown(self) -> None:
        """ teardown method """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_create_class(self):
        """ Tests if the class was created correctly """
        p1 = Place()
        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "city_id"))
        self.assertTrue(hasattr(p1, "user_id"))
        self.assertTrue(hasattr(p1, "name"))
        self.assertTrue(hasattr(p1, "description"))
        self.assertTrue(hasattr(p1, "number_rooms"))
        self.assertTrue(hasattr(p1, "number_bathrooms"))
        self.assertTrue(hasattr(p1, "max_guest"))
        self.assertTrue(hasattr(p1, "price_by_night"))
        self.assertTrue(hasattr(p1, "latitude"))
        self.assertTrue(hasattr(p1, "longitude"))
        self.assertTrue(hasattr(p1, "amenity_ids"))

    def test_empty_attributes(self):
        """ Tests if the atribute its empty """
        p1 = Place()
        self.assertAlmostEqual(p1.city_id, "")
        self.assertAlmostEqual(p1.user_id, "")
        self.assertAlmostEqual(p1.name, "")
        self.assertAlmostEqual(p1.description, "")
        self.assertAlmostEqual(p1.number_rooms, 0)
        self.assertAlmostEqual(p1.number_bathrooms, 0)
        self.assertAlmostEqual(p1.max_guest, 0)
        self.assertAlmostEqual(p1.price_by_night, 0)
        self.assertAlmostEqual(p1.latitude, 0.0)
        self.assertAlmostEqual(p1.longitude, 0.0)
        self.assertAlmostEqual(p1.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
