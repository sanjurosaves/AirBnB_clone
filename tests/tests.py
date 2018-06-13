#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User


class TestBaseModel(unittest.TestCase):
    """class to test base model"""
    def test_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

class TestUser(unittest.TestCase):
    """class to test User class"""
    def test_uuid(self):
        u1 = User()
        u2 = User()
        self.assertIsInstance(u1, User)
        self.assertTrue(hasattr(u1, "id"))
        self.assertNotEqual(u1.id, u2.id)
        self.assertIsInstance(u1.id, str)
