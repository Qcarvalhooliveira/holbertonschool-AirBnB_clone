#!/usr/bin/python3
""" unittest for BaseModel class"""

import pep8
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for base_model module and BaseModel class"""
    @classmethod
    def setUpClass(cls):
        """ set up base class"""
        cls.base = BaseModel()

    @classmethod
    def teardown(cls):
        del cls.base

    def test_pep8_conformance_test_base_model(self):
        """ Test that test_base_model.py follows pep8 standardization"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or warnings")

    def test_save(self):
        """Test public method save() for class BaseModel"""
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """Test that to_dict() creates a dictionary object of an instance"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
