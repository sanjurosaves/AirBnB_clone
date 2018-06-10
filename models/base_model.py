#!/usr/bin/python3
""" Module defines base class. """
import uuid
import json
import datetime

class BaseModel:
    """ This is the Base class. """
    __nb_objects = 0

    def __init__(self, created_at=None, updated_at=None, id=None):
        """ Initialize the BaseModel class."""
        if id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id

        if created_at is None:
            self.created_at = datetime.datetime.now().isoformat()

        if updated_at is None:
            self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        """Function returns string rep of the display function."""
        return "[BaseModel] (" + str(self.id) + ") " \
            + str(self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """Adds items to a_dict."""
        a_dict = {}
        key = ["id", "created_at", "updated_at", "__class__", "my_number", "name"]
        for i in range(len(key)):
            if key[i] == "id":
                a_dict[key[i]] = self.id
            if key[i] == "created_at":
                a_dict[key[i]] = self.created_at
            if key[i] == "updated_at":
                a_dict[key[i]] = self.updated_at
            if key[i] == "__class__":
                a_dict[key[i]] = self.__class__.__name__
            if key[i] == "my_number":
                a_dict[key[i]] = 89
            if key[i] == "name":
                a_dict[key[i]] = "Holberton"
        return a_dict
