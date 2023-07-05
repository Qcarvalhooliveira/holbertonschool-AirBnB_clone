#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """
    Test cases for User class
    """
    def test_user_inherits_from_base_model(self):
        """
        Test if User class inherits from BaseModel class
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_attributes(self):
        """
        Test if User class has the correct attributes
        """
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_initialization(self):
        """
        Test if User class can be initialized with arguments
        """
        user = User(email='test@example.com', password='123456')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, '123456')

    def test_user_to_dict(self):
        """
        Test if User instance can be converted to a dictionary
        """
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(type(user_dict), dict)
        self.assertEqual(user_dict['__class__'], 'User')

    def test_user_from_dict(self):
        """
        Test if User instance can be created from a dictionary
        """
        user_data = {
            'email': 'test@example.com',
            'password': '123456',
            'first_name': 'Queise',
            'last_name': 'Carvalho'
        }
        user = User(**user_data)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, '123456')
        self.assertEqual(user.first_name, 'Queise')
        self.assertEqual(user.last_name, 'Carvalho')


if __name__ == '__main__':
    unittest.main()
