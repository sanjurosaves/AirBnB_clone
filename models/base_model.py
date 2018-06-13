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
            if hasattr(self, 'created_at'):
                self.created_at = datetime.datetime(
                    *map(int, re.split('[^\d]', self.created_at)[:]))
                self.updated_at = datetime.datetime(
                    *map(int, re.split('[^\d]', self.updated_at)[:]))

        else:
            self.new_inst()

    def __str__(self):
        """Function returns string rep of the display function."""
        return ("[" + str(type(self).__name__) + "]" + " (" + str(self.id) +
                ") " + str(self.__dict__))

    def new_inst(self):
        """creates new instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)

    def save(self):
        """saves instance"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Adds items to a_dict."""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = datetime.datetime.isoformat(
            self.__dict__['created_at'])
        new_dict['updated_at'] = datetime.datetime.isoformat(
            self.__dict__['updated_at'])
        return new_dict
