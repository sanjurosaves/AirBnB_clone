#!/usr/bin/python3
import os
import pep8
import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User


class TesHBNBCommand(unittest.TestCase):
    """Testing console class"""

    def test_pep8(self):
        """test for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['console.py'])
        self.assertEqual(p.total_errors, 0, 'pep8 error(s) in console.py')
        p = style.check_files(['tests/test_console.py'])
        self.assertEqual(p.total_errors, 0, 'pep8 error(s) in test_console.py')

    def test_emptyline(self):
        pass

    def test_do_quit(self):
        pass

    def test_do_EOF(self):
        pass

    def test_do_create(self):
        pass
#        res = do_create("create")
#        self.assertEqual("** class doesn't exist **")
