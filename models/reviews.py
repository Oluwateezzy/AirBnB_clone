#!/usr/bin/python3
""" Review """
from models.base_model import BaseModel


class Reviews(BaseModel):
    """ construct """
    place_id = ""
    user_id = ""
    text = ""
