#!/usr/bin/python3
"""
test user
"""

import unittest as unt
from models.user import User as us


class TestUser(unt.TestCase):
    """test User"""

    def test_att(self):
        """test for User attributes"""

        mdl = us()
        self.assertEqual(mdl.first_name, '')
        self.assertEqual(mdl.password, '')
        self.assertEqual(mdl.last_name, '')
        self.assertEqual(mdl.email, '')
