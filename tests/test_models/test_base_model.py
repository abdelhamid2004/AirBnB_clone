#!.usr.bin.python3
'''
Test base model class
'''

import unittest
from models.base_model import BaseModel as bs


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        mdl = bs()
        self.assertIsNotNone(mdl.id)
        self.assertIsNotNone(mdl.created_at)
        self.assertIsNotNone(mdl.updated_at)

    def test_save(self):
        mdl = bs()
        first_up = mdl.updated_at
        new_up = mdl.save()
        self.assertNotEquals(first_up, new_up)

    def test_dict(self):
        mdl = bs()
        mdldic = mdl.to_dict()
        self.assertIsInstance(mdldic, dict)
        self.assertEquals(mdldic["__class__"], "BaseeModel")
        self.assertEquals(mdldic["id"], mdl.id)
        self.assertEquals(mdldic["created_at"], mdl.created_at.isoformat())
        self.assertEquals(mdldic["updated_at"], mdl.updated_at.isoformat())

    def test_str(self):
        mdl = bs()
        self.assertTrue(str(mdl).startswith("'[BaseeModel]'"))
        self.assertIn(mdl.id, str(mdl))
        self.assertIn(str(mdl.__dict__), str(mdl))


if __name__ == "__main__":
    unittest.main()
