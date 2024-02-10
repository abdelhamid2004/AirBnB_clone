#!/usr/bin/python3
"""BaseModel"""

from models.base_model import BaseModel as bs


class Place(bs):
    """inherits BaseModel"""

    user_id = ""
    city_id = ""
    number_rooms = 0
    number_bathrooms = 0
    name = ""
    description = ""
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    max_guest = 0
    price_by_night = 0
