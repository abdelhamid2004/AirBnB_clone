#!/usr/bin/python3
"""
review testing
"""

import unittest as unt
from models.review import Review as re


class TestReview(unt.TestCase):
    """check Review"""

    def test_attr(self):
        """chek Review attributes"""

        mdl = re()
        self.assertEqual(mdl.user_id, '')
        self.assertEqual(mdl.text, '')
        self.assertEqual(mdl.place_id, '')
