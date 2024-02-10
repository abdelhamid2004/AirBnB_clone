#!/usr/bin/python3
"""
test citu class
"""

import unittest as unt
from models.city import City as ct


class TestCity(unt.TestCase):
    """City class testing"""

    def test_att(self):
        """checking City attributes"""

        mdl = ct()
        self.assertEqual(mdl.name, '')
        self.assertEqual(mdl.state_id, '')
