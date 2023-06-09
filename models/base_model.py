#!/usr/bin/python3
""" BaseModel """
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    defines all common attributes for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        string representation of the class
        """
        return "[{}] ({}) {}".format(type(self).__name__, str(self.id), str(self.__dict__))

    def save(self):
        """
        save state
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        create a dict of the object
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
