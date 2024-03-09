import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_attributes(self):
        # Test that id, created_at, and updated_at are initialized properly
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        # Test __str__ method
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        # Test save method
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_method(self):
        # Test to_dict method
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

    def test_create_instance_from_dict(self):
        # Test creating an instance from dictionary
        data = {
            'id': '123',
            'created_at': '2024-03-09T12:00:00.000000',
            'updated_at': '2024-03-09T12:00:00.000000'
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, '123')
        self.assertEqual(model.created_at.isoformat(), '2024-03-09T12:00:00')
        self.assertEqual(model.updated_at.isoformat(), '2024-03-09T12:00:00')

if __name__ == '__main__':
    unittest.main()
