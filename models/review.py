#!/usr/bin/python3
""" module defines Review  class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class inherits BaseModel and defines the Review."""
    place_id = ""
    user_id = ""
    text = ""
