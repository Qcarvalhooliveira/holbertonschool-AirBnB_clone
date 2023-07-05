#!/usr/bin/python3
"""Module that initialize the models package"""

from base_model import BaseModel
from file_storage import FileStorage

storage = FileStorage()
storage.reload()
