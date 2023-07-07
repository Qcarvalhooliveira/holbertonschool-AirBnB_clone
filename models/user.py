#!/usr/bin/python3
"""
Module for class User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
