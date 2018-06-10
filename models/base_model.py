#!/usr/bin/python3
""" Module defines base class. """
import uuid
import json
import datetime

class BaseModel:
    """ This is the Base class. """

    def __init__(self, *args, **kwargs):
        """ Initialize the BaseModel class."""
#        if len(kwargs) != 0:
#            to_dict(**kwargs)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Function returns string rep of the display function."""
        return "[BaseModel] (" + str(self.id) + ") " \
            + str(self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Adds items to a_dict."""
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
