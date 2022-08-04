#!/usr/bin/python3
""" base_model.py - BaseModel """
import models
from uuid import uuid4
import datetime


class BaseModel(object):
    """ define all common attribute/methods """
    def __init__(self):
        """
        """
        self.id = str(uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Return:
            prints when the print function call
        """
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        """
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """
        Returns:
            dictionary containd all key/values
            class name
            the updated and created at of the instance iso format
        """
        dictionary = dict(self.__dict__)
        dictionary.update({"__class__": self.__class__.__name__})
        dictionary.update({"created_at": self.created_at.isoformat()})
        dictionary.update({"updated_at": self.updated_at.isoformat()})

        return dictionary
