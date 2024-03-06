#!/usr/bin/python3
"""  """


class FileStorage:
        """
            serializes instances to a JSON file and deserializes
        """
        __file_path = 'test'
        __objects = 'test'

        def all(self):
            """ returns the dict __objects """
            return self.__objects

        def new(self, obj):
            """ sets in __objects the obj with key <obj class name>.id """
            self.__class__.__objects[self.__class__.__name__] = obj
