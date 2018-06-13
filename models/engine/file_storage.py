#!/usr/bin/python3
""" serializes instances to JSON file & deserializes JSON file to instances """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        id_obj = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[id_obj] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        filename = FileStorage.__file_path
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(filename, mode='w', encoding='utf-8') as a_file:
            json.dump(new_dict, a_file)

    def reload(self):
        """ deserializes the JSON file to __objects (if JSON file exists) """
        filename = FileStorage.__file_path
        try:
            with open(filename, encoding='utf-8') as a_file:
                new_obj = json.load(a_file)
            for key, value in new_obj.items():
                class_name = value['__class__']
                self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
