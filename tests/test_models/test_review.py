#!/usr/bin/python3
"""
Unittest for Review class
"""
import unittest
from models.review import Review
import os


class TestReview(unittest.TestCase):
    """ Tests for Review Class"""

    def tearDown(self) -> None:
        """ teardown method """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_create_class(self):
        """ Tests if the class was created correctly """
        r1 = Review()
        self.assertIsInstance(r1, Review)
        self.assertTrue(hasattr(r1, "place_id"))
        self.assertTrue(hasattr(r1, "user_id"))
        self.assertTrue(hasattr(r1, "text"))

    def test_empty_attributes(self):
        """ Tests if the atribute its empty """
        r1 = Review()
        self.assertAlmostEqual(r1.place_id, "")
        self.assertAlmostEqual(r1.user_id, "")
        self.assertAlmostEqual(r1.text, "")


if __name__ == "__main__":
    unittest.main()
