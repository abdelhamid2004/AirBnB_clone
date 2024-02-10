#!/usr/bin/python3
"""
state testing
"""

import unittest as unt
from models.state import State as st


class TestState(unt.TestCase):
    """testing State"""

    def test_attr(self):
        """check State attributes"""

        mdl = st()

        self.assertEqual(mdl.name, '')
