#!/usr/bin/python3
'''
base class
'''


from models import storage as st
from uuid import uuid4 as ud
from datetime import datetime as dt


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):

        if kwargs:
            for k, val in kwargs.items():
                if k != '__class__':
                    if k == 'updated_at' or k == 'created_at':
                        self.__dict__[k] = dt.fromisoformat(val)
                    else:
                        self.__dict__[k] = val
        else:
            self.id = str(ud())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            st.new(self)

    def to_dict(self):
        """returns a dictionary of values"""

        dicto = dict(self.__dict__)
        dicto['__class__'] = self.__class__.__name__
        dicto['created_at'] = \
            dt.isoformat(dicto.get('created_at'))
        dicto['updated_at'] = \
            dt.isoformat(dicto.get('updated_at'))
        return dicto

    def __str__(self) -> str:   
        nm = self.__class__.__name__
        return "[{}] ({}) {}".format(nm, self.id, self.__dict__)

    def save(self):
        """update instance"""

        self.updated_at = dt.now()
        st.new(self)
        st.save()
