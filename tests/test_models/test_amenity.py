#!/usr/bin/python3
"""
Amenity testing
"""

import unittest as unt
from models.amenity import Amenity as am


class testt_am(unt.TestCase):
    """Amenity testing"""

    def test_att(self):
        """check Amenity attributes"""

        mdl = am()

        self.assertEqual(mdl.name, '')