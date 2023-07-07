#!/usr/bin/python3
"""
Unittest for Review class
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from models.user import User
from models.place import Place


class TestReview(unittest.TestCase):
    """
    Test cases for Review class
    """
    def test_inheritance(self):
        """
        Test if Review class inherits from BaseModel
        """
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """
        Test if the attributes are correctly initialized
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_initialization(self):
        """
        Test if the attributes are correctly initialized with specific values
        """
        review = Review(place_id="123", user_id="456", text="Good place!")
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Good place!")


if __name__ == '__main__':
    unittest.main()
