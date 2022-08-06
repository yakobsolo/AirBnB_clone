#!/usr/bin/python3
""" user.py - User"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    user class
    """
    email = ""
    first_name = ""
    last_name = ""
    password = ""
