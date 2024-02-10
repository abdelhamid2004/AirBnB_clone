#!/usr/bin/python3
"""BaseModel module"""

from models.base_model import BaseModel as bs


class City(bs):
    """inherits BaseModel"""

    name = ""
    state_id = ""
