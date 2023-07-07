#!/usr/bin/python3
"""Module for class FileStorage"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
           "State": State, "City": City, "Amenity": Amenity, "Review": Review}


class FileStorage:
    """Class that serializes instances to a JSON file and d
       eserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        new_json = {}
        for key in self.__objects:
            new_json[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as myFile:
            json.dump(new_json, myFile)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as file:
                json_data = file.read()
                object_dict = json.loads(json_data)

            for key, value in object_dict.items():
                class_name = value["__class__"]
                cls = classes[class_name]
                obj = cls(**value)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
