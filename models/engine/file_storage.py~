#!/usr/bin/python3
""" serializes instances to JSON file & deserializes JSON file to instances """
import json
from models.base_model import BaseModel


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        id_obj = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[id_obj] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        serialized = __objects.to_json()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as a_file:
            return json.dump(serialized, a_file)

    def reload(self):
        """ deserializes the JSON file to __objects (if JSON file exists) """
        pass
