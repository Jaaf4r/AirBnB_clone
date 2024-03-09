#!/usr/bin/python3
from unittest import TestCase
from models.base_model import BaseModel
import os
import json
from models.engine.file_storage import FileStorage


class TestFileStorage(TestCase):
    def setUp(self):
        self.f1 = FileStorage()
        self.b1 = BaseModel()
        self.file_path = "file.json"
        self.object = {"BaseModel.123": {"id": "123", "name": "test"}}

        with open(self.file_path, "w") as f:
            json.dump(self.object, f)

    def test_atributes(self):
        self.assertIsInstance(self.f1._FileStorage__file_path, str)
        self.assertIsInstance(self.f1._FileStorage__objects, dict)

    def test_new(self):
        self.assertIn(self.b1, self.f1.all().values())

    def test_save(self):
        self.f1.new(self.b1)
        self.f1.save()

        with open(self.file_path, "r") as f:
            read_data = f.read()
            name = self.b1.__class__.__name__
        self.assertIn("{}.{}".format(name, self.b1.id), read_data)

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except IOError:
            pass
