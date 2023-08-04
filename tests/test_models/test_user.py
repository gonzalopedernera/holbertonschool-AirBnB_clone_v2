#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from models.user import User
import os


class TestUser(unittest.TestCase):
    """ Tests for User Class"""

    def tearDown(self) -> None:
        """ teardown method """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_create_class(self):
        """ Tests if the class was created correctly """
        u1 = User()
        self.assertIsInstance(u1, User)
        self.assertTrue(hasattr(u1, "email"))
        self.assertTrue(hasattr(u1, "password"))
        self.assertTrue(hasattr(u1, "first_name"))
        self.assertTrue(hasattr(u1, "last_name"))

    def test_empty_attributes(self):
        """ Tests if the atribute its empty """
        u1 = User()
        self.assertAlmostEqual(u1.email, "")
        self.assertAlmostEqual(u1.password, "")
        self.assertAlmostEqual(u1.first_name, "")
        self.assertAlmostEqual(u1.last_name, "")


if __name__ == "__main__":
    unittest.main()
