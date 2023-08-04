#!/usr/bin/python3
"""
Unittest for the console
"""
import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from io import StringIO
import os
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """ Tests for the console """

    def setUp(self) -> None:
        self.cmd = HBNBCommand()
        self.base_model = BaseModel()

    def tearDown(self) -> None:
        """ teardown method """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_help(self):
        """ tests the help function """
        with patch('sys.stdout', new=StringIO()) as screen:
            HBNBCommand().onecmd("help")
            text = """
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

"""
            self.assertEqual(text, screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            HBNBCommand().onecmd("help EOF")
            self.assertAlmostEqual(
                "Exits the program with EOF\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            HBNBCommand().onecmd("help all")
            self.assertAlmostEqual(
                "Shows all the instances or only the given one\n",
                screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            HBNBCommand().onecmd("help create")
            self.assertAlmostEqual(
                "Creates an instance for the input class sent\n",
                screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            HBNBCommand().onecmd("help destroy")
            self.assertAlmostEqual(
                "Destroys the specific instance for the given ID\n",
                screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            HBNBCommand().onecmd("help help")
            self.assertAlmostEqual("", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            HBNBCommand().onecmd("help quit")
            self.assertAlmostEqual(
                "Quit command to exit the program\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            HBNBCommand().onecmd("help show")
            self.assertAlmostEqual(
                "Shows the specific instance for the given ID\n",
                screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            HBNBCommand().onecmd("help update")
            self.assertAlmostEqual(
                "Updated an instance for the given id\n", screen.getvalue())

    def test_quit(self):
        """ test quit function """
        with patch("sys.stdout", new=StringIO()) as screen:
            self.assertTrue(self.cmd.onecmd("quit"))

    def test_create(self):
        """ test create function """
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("create")
            self.assertAlmostEqual(
                "** class name missing **\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("create MyModel")
            self.assertAlmostEqual(
                "** class doesn't exist **\n", screen.getvalue())

    def test_show(self):
        """ test show function """
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("show")
            self.assertAlmostEqual(
                "** class name missing **\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("show MyModel")
            self.assertAlmostEqual(
                "** class doesn't exist **\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("show BaseModel")
            self.assertAlmostEqual(
                "** instance id missing **\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("show BaseModel 1234")
            self.assertAlmostEqual(
                "** no instance found **\n", screen.getvalue())

    def test_destroy(self):
        """ test destroy function """
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("destroy")
            self.assertAlmostEqual(
                "** class name missing **\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("destroy MyModel")
            self.assertAlmostEqual(
                "** class doesn't exist **\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("destroy BaseModel")
            self.assertAlmostEqual(
                "** instance id missing **\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("destroy BaseModel 1234")
            self.assertAlmostEqual(
                "** no instance found **\n", screen.getvalue())

    def test_all(self):
        """ test all function"""
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("all")
            self.assertAlmostEqual(
                '["{}"]\n'.format(str(self.base_model)), screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("all BaseModel")
            self.assertAlmostEqual(
                '["{}"]\n'.format(str(self.base_model)), screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("show MyModel")
            self.assertAlmostEqual(
                "** class doesn't exist **\n", screen.getvalue())

    def test_update(self):
        """ test update function """
        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("update")
            self.assertAlmostEqual(
                "** class name missing **\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("update MyModel")
            self.assertAlmostEqual(
                "** class doesn't exist **\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("update BaseModel")
            self.assertAlmostEqual(
                "** instance id missing **\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd("update BaseModel 1234")
            self.assertAlmostEqual(
                "** no instance found **\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd(
                "update BaseModel {}".format(self.base_model.id))
            self.assertAlmostEqual(
                "** attribute name missing **\n", screen.getvalue())

        with patch("sys.stdout", new=StringIO()) as screen:
            self.cmd.onecmd(
                "update BaseModel {} name".format(self.base_model.id))
            self.assertAlmostEqual(
                "** value missing **\n", screen.getvalue())


if __name__ == "__main__":
    unittest.main()
