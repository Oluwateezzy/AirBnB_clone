#!/usr/bin/python3
""" testing files
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
import pep8


class BaseModel_testing(unittest.TestCase):
    """ check BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        rest = pepstylecode.check_files(['models/base_model.py',
                                         'models/__init__.py'])
        self.assertEqual(rest.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_for_base_model(unittest.TestCase):
    """ Class test for BaseModel """
    my_model = BaseModel()

    def SetUp(self):
        """ Create instance """
        self.test = BaseModel()

    def test_attr_none(self):
        """None attribute."""
        object_test = BaseModel(None)
        self.assertTrue(hasattr(object_test, "id"))
        self.assertTrue(hasattr(object_test, "created_at"))
        self.assertTrue(hasattr(object_test, "updated_at"))

    def test_str(self):
        """ Test string """
        dictonary = {'id': 'cc9909cf-a909-9b90-9999-999fd99ca9a9',
                     'created_at': '2025-06-28T14:00:00.000001',
                     '__class__': 'BaseModel',
                     'updated_at': '2030-06-28T14:00:00.000001',
                     'score': 100
                     }

        object_test = BaseModel(**dictonary)
        out = "[{}] ({}) {}\n".format(type(object_test).__name__, object_test.id, object_test.__dict__)

    def test_datetime(self):
        """ check datatime """
        bas1 = BaseModel()
        self.assertFalse(datetime.now() == bas1.created_at)

    def test_BaseModel(self):
        """ check attributes values in a BaseModel """

        self.my_model.name = "Holbie"
        self.my_model.my_number = 100
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])
