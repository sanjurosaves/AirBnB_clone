#!/usr/bin/python3
""" module defines City class """
from models.base_model import BaseModel


class City(BaseModel):
    """This class inherits BaseModel and defines the City."""
    state_id = ""
    name = ""
