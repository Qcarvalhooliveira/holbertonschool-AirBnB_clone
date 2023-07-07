#!/usr/bin/python3
"""
Unittest for place class
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity


class TestPlace(unittest.TestCase):
    """
    Test cases for Place class
    """
    def test_inheritance(self):
        """
        Test if Place class inherits from BaseModel
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        """
        Test if the attributes are correctly initialized
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_initialization(self):
        """
        Test if the attributes are correctly initialized with specific values
        """
        place = Place(city_id="123", user_id="456", name="Cozy Apartment",
                      description="Beautiful apartment in the city center",
                      number_rooms=2, number_bathrooms=1, max_guest=4,
                      price_by_night=100, latitude=37.7749,
                      longitude=-122.4194,
                      amenity_ids=["amenity1", "amenity2"])
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Cozy Apartment")
        self.assertEqual(place.description,
                         "Beautiful apartment in the city center")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])


if __name__ == '__main__':
    unittest.main()
