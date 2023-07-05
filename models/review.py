#!/usr/bin/python3
"""
Module for review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
