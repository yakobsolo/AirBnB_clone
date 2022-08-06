#!/usr/bin/python3
""" file_storage.py - FileStorage """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    private class attribute
    and public methods
    """
    __file_path = "file.json"
    __objects = {}
    clas = {"BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def all(self):
        """
        Return: __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        creates new __objects
        """
        obj_key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """
        serializes python object to json file
        """
        dict = {}
        for i, j in FileStorage.__objects.items():
            dict[i] = j.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict, f)

    def reload(self):
        """
        deserializes json file to python object
        """
        try:
            with open(FileStorage.__file_path) as f:
                new_dict = json.load(f)
            for i, j in new_dict.items():
                obj = FileStorage.clas[j["__class__"]](**j)
                FileStorage.__objects[i] = obj
        except FileNotFoundError:
            pass
