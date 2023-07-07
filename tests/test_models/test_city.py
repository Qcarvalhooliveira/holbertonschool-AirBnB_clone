#!/usr/bin/python3
"""
Unittest for city class
"""
import unittest
from models.city import City
from models.base_model import BaseModel
from models.state import State



class TestCity(unittest.TestCase):
    def test_inheritance(self):
        """
        Test if City class inherits from BaseModel
        """
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """
        Test if the attributes are correctly initialized
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_initialization(self):
        """
        Test if the attributes are correctly initialized with specific values
        """
        city = City(state_id="123", name="San Francisco")
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "San Francisco")


if __name__ == '__main__':
    unittest.main()
