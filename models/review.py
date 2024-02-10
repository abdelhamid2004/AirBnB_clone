#!/usr/bin/python3
"""BaseModel"""

from models.base_model import BaseModel as bs


class Review(bs):
    """inherits BaseModel"""

    user_id = ""
    text = ""
    place_id = ""