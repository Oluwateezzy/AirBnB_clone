#!/usr/bin/python3
""" User model """
from models.base_model import BaseModel


class User(BaseModel):
    """ construct """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
