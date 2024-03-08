#!/usr/bin/python3
"""
Module: file_storage.py

Defines a `FileStorage` class.
"""
import os
import json
from models.base_model import BaseModel


class FileStorage():
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    #__file_path = "file.json"
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON
        file exists; otherwise, does nothing
        """
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as f:
                    dict = json.loads(f.read())
                    for value in dict.values():
                        cls = value["__class__"]
                        self.new(eval(cls)(**value))
            except Exception:
                pass
