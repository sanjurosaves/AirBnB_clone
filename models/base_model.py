#!/usr/bin/python3
""" Module defines base class. """
import uuid
import json
import datetime
import re
import models

class BaseModel:
    """ This is the Base class. """

    def __init__(self, *args, **kwargs):
        """ Initialize the BaseModel class."""
        if len(kwargs) != 0:
            self.__dict__ = kwargs
            self.created_at = datetime.datetime\
                              (*map(int, re.split('[^\d]',\
                                                  self.created_at)[:]))
            self.updated_at = datetime.datetime\
                              (*map(int, re.split('[^\d]',\
                                                  self.updated_at)[:]))

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Function returns string rep of the display function."""
        return "[BaseModel] (" + str(self.id) + ") " \
            + str(self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Adds items to a_dict."""
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
