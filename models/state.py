#!/usr/bin/python3
"""
Module for state User
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class representing a state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
