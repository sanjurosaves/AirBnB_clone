#!/usr/bin/python3
import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User


class TestBaseModel(unittest.TestCase):
    """class to test base model"""
    def test_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

class TestUser(unittest.TestCase):
    """class to test User class"""
    def test_uuid(self):
        u1 = User()
        u2 = User()
        self.assertIsInstance(u1, User)
        self.assertTrue(hasattr(u1, "id"))
        self.assertTrue(hasattr(u1, "email"))
        self.assertTrue(hasattr(u1, "password"))
        self.assertTrue(hasattr(u1, "first_name"))
        self.assertTrue(hasattr(u1, "last_name"))
        self.assertNotEqual(u1.id, u2.id)
        self.assertIsInstance(u1.id, str)

class TestConsole(unittest.TestCase):
    """class to test console functions"""
    def test_emptyline(self):
        pass

    def test_do_quit(self):
        pass

    def test_do_EOF(self):
        pass

    def test_do_create(self):
        pass

if __name__ == '__main__':
    unittest.main()
