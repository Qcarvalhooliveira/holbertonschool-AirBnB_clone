#!/usr/bin/python3
"""
Module for amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing an amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
