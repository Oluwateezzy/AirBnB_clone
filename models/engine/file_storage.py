#!/usr/bin/python3
"""storage"""
import json
import uuid
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.reviews import Reviews
from datetime import datetime


class FileStorage:
    __file_path = "file.json"
    __objects =  {}

    def all(self):
        """ return all object """
        return FileStorage.__objects
    
    def new(self, obj):
        """ set in objects """
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """ save object """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            new_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            json.dump(new_dict, file)

    def reload(self):
        """ reload object """
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                json_file = json.load(file)
                for key, value in json_file.items():
                    FileStorage.__objects[key] = eval(
                            value['__class__'])(**value)
