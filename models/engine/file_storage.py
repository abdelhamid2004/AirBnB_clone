#!/usr/bin/python3
""" json file"""


import json as js


class FileStorage:
    """json file"""

    __file_path = 'file.json'
    __objects = {}

    def save(self):
        """save in the path .json"""

        with open(self.__file_path, "w", encoding='utf-8') as file_name:
            dicto = {}
            for k, val in self.__objects.items():
                dicto[k] = val.to_dict()
            js.dump(dicto, file_name)

    def new(self, obj):
        """ assin a new value for object """

        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def reload(self):
        """"__objects to json"""

        from models.base_model import BaseModel as bs
        from models.user import User as us
        from models.city import City as ci
        from models.state import State as st
        from models.amenity import Amenity as am
        from models.review import Review as re
        from models.place import Place as pl

        n_list = {
                    "User": us, "BaseModel": bs, "City": ci,
                    "State": st, "Amenity": am, "Review": re,
                    "Place": pl
                }
        try:
            with open(self.__file_path, "r", encoding='utf-8') as file_name:
                dicto = js.load(file_name)
                for val in dicto.values():
                    self.new(n_list[val['__class__']](**val))
        except FileNotFoundError:
            pass

    def all(self):
        """dictionary __objects"""

        return self.__objects
