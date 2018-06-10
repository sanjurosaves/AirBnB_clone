#!/usr/bin/python3
"""
Module defines base class.
"""
import json
import datetime

class BaseModel:
    """
    This is the Base class.
    """
    __nb_objects = 0

    def __init__(self, id=None, created_at, updated_at):
        """ Initialize the BaseModel class."""
        self.id = id
        self.created_at = datetime.datetime.now
        self.update_at = datetime.datetime.now
        self.y = y

    def __str__(self):
        """Function returns string rep of the display function."""
        return "[BaseModel] (" + str(self.id) + ") " \
            + str(self.__dict__)

    def to_dict(self):
        """Adds items to a_dict."""
        a_dict = {}
        key = ["id", "created_at", "updated_at", "__class__"]
        for i in range(len(key)):
            if key[i] == "id":
                a_dict[key[i]] = self.id
            if key[i] == "created_at":
                a_dict[key[i]] = self.created_at
            if key[i] == "updated_at":
                a_dict[key[i]] = self.updated_at
            if key[i] == "__class__":
                a_dict[key[i]] = self.__class__
        return a_dict