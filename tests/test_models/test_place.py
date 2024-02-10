#!/usr/bin/python3
"""
place class testing
"""

import unittest as unt
from models.place import Place as pl


class TestPlace(unt.TestCase):
    """Place testing"""

    def test_att(self):
        """checking Place attributes"""

        mdl = pl()
        self.assertEqual(mdl.user_id, '')
        self.assertEqual(mdl.name, '')
        self.assertEqual(mdl.description, '')
        self.assertEqual(mdl.price_by_night, 0)
        self.assertEqual(mdl.latitude, 0.0)
        self.assertEqual(mdl.longitude, 0.0)
        self.assertEqual(mdl.amenity_ids, [])
        self.assertEqual(mdl.city_id, '')
        self.assertEqual(mdl.number_rooms, 0)
        self.assertEqual(mdl.number_bathrooms, 0)
        self.assertEqual(mdl.max_guest, 0)
