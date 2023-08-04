#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import MySQLdb
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        db = MySQLdb.connect(host="localhost",
                             database="hbnb_dev_db",
                             user="hbnb_dev",
                             password="hbnb_dev_pwd")
        self.cursor = db.cursor()

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        old_lenght = len(storage.all())
        new = BaseModel()
        new.save()
        storage.save()
        new_lenght = len(storage.all())
        self.assertTrue(old_lenght + 1 == new_lenght)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        new.save()
        storage.save()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_delete(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        new.save()
        storage.save()
        old_lenght = len(storage.all())
        storage.delete(new)
        new_lenght = len(storage.all())
        self.assertTrue(old_lenght - 1 == new_lenght)
