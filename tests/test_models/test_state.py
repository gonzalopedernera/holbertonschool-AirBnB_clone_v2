#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models import storage
import MySQLdb


class test_state(test_basemodel):
    """ """

    def setUp(self):
        """ Set up test environment """
        db = MySQLdb.connect(host="localhost",
                             database="hbnb_dev_db",
                             user="hbnb_dev",
                             password="hbnb_dev_pwd")
        self.cursor = db.cursor()

    def test_name3(self):
        """ check for state creation """
        new = State(name="Alabama")
        new.save()
        storage.save()
        relational = self.cursor.execute(
            "SELECT * FROM states WHERE id = %s", (new.id))
        self.assertEqual(relational == new)
