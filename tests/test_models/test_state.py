#!/usr/bin/python3
"""
Unittest for state class
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_inheritance(self):
        """
        Test if State class inherits from BaseModel
        """
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """
        Test if the attributes are correctly initialized
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_initialization(self):
        """
        Test if the attributes are correctly initialized with specific values
        """
        state = State(name="California")
        self.assertEqual(state.name, "California")


if __name__ == '__main__':
    unittest.main()
