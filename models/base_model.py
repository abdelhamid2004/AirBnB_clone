#!/usr/bin/pyhton3
'''
Parent class to all other classes
'''

import uuid as ud
from datetime import datetime as dt


class BaseeModel:
    def __init__(self):
        self.id = str(ud.uuid4())
        self.created_at = dt.utcnow()
        self.updated_at = dt.utcnow()

    def save(self):
        '''
        Updated updated at
        '''

        self.updated_at = dt.utcnow()

    def to_dict(self):
        '''
        get the dictinary of the class
        :return: dict to the values
        '''
        dict = self.__dict__.copy()
        dict["__clase__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict

    def __str__(self):
        '''
        :return: string of that class
        '''
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)


if __name__ == "__main__":
    mdl = BaseeModel()
    mdl.name = "my first model"
    mdl.num = 89
    print(mdl)
    mdl.save()
    print(mdl)
    mdljs = mdl.to_dict()
    print(mdljs)
    print("sdsds")
    for key in mdljs.keys():
        print(key)
