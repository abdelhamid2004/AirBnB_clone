#!/usr/bin/python3
"""
basemodel testing
"""


from models import storage as st
import unittest as unt
from datetime import datetime as dt
from models.base_model import BaseModel as bs
from models.engine.file_storage import FileStorage as filstor


class TestFilstor(unt.TestCase):
    """testing"""

    def test_stor(self):
        """storage testing"""

        all_objs = st.all()
        for ids in all_objs.keys():
            ob = all_objs[ids]

        try:
            with open("file.json", "r", encoding='utf-8') as file:
                self.assertIsInstance(all_objs, dict)
                self.assertIsInstance(ob, bs)
                self.assertEqual(f"{ob}",
                                 f"{ob.__class__.__name__}.{ob.id}")
                value = f"[{ob.__class__.__name__}] ({ob.id}) {ob.__dict__}"
                self.assertEqual(str(ob), value)

        except FileNotFoundError:
            self.assertIsInstance(all_objs, dict)
            self.assertEqual(all_objs, {})

        mdl = bs()
        mdl.my_number = 89
        mdl.name = "My_First_Model"
        mdl.save()
