#!/usr/bin/python3
""" The Review Model """
from models.base_model import BaseModel

class Review(BaseModel):
    """ Review Class"""
    place_id = ""
    user_id = ""
    text = ""
