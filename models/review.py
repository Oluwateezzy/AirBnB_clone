#!/usr/bin/python3
""" Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ construct """
    place_id = ""
    user_id = ""
    text = ""
