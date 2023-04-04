#!/usr/bin/env python3
""" BaseModel """
import uuid
import models
from datetime import datetime


class BaseModel:
    """
    defines all common attributes for other classes
    """

    def __init__(self):
        """
        Constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

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

    def to_dict(self):
        """
        create a dict of the object
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
