#!.usr.bin.python3
'''
Test base model class
'''

import unittest
from models.base_model import BaseeModel


class TestBaseModel(unittest.TestCase):
    def tst_init(self):
        mdl = BaseeModel()
        self.assertIsNotNone(mdl.id)
        self.assertIsNotNone(mdl.created_at)
        self.assertIsNotNone(mdl.updated_at)

    def tst_save(self):
        mdl = BaseeModel()
        first_up = mdl.updated_at
        new_up = mdl.save()
        self.assertNotEquals(first_up, new_up)

    def tst_dict(self):
        mdl = BaseeModel()
        mdldic = mdl.to_dict()
        self.assertIsInstance(mdldic, dict)
        self.assertEquals(mdldic["__clase__"], "BaseeModel")
        self.assertEquals(mdldic["id"], mdl.id)
        self.assertEquals(mdldic["created_at"], mdl.created_at.isoformat())
        self.assertEquals(mdldic["updated_at"], mdl.updated_at.isoformat())

    def tst_str(self):
        mdl = BaseeModel()
        self.assertTrue(str(mdl).startswith("['BaseeModel']"))
        self.assertIn(mdl.id, str(mdl))
        self.assertIn(str(mdl.__dict__), str(mdl))


if __name__ == "__main__":
    unittest.main()
