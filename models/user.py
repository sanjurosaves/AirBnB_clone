#!/usr/bin/python3
""" module defines User class """
from models.base_model import BaseModel


class User(BaseModel):
    """define User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
