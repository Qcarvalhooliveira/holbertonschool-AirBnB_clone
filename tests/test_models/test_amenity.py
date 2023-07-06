#!/usr/bin/python3
"""
Unittest for amenity class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test cases for Place class
    """
    def test_inheritance(self):
        """
        Test if Amenity class inherits from BaseModel
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """
        Test if the attributes are correctly initialized
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_initialization(self):
        """
        Test if the attributes are correctly initialized with specific values
        """
        amenity = Amenity(name="Wifi")
        self.assertEqual(amenity.name, "Wifi")


if __name__ == '__main__':
    unittest.main()
