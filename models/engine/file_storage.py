#!/usr/bin/python3
"""
This module defines the FileStorage class
"""
import json
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON."""
    # The path of the JSON file where the objects are stored
    __file_path = "file.json"
    # A dictionary containing all the objects
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects.
        Args:
            self (FileStorage): the current instance
        Returns:
            dict: the dictionary __objects
        """
        # Just return __objects
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id.
        Args:
            self (FileStorage): the current instance
            obj (BaseModel): the object to add to __objects
        """
        # The key is created by concatenating the class name and id of the obj
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        # The object is added to the dictionary
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file (path: __file_path).
        Args:
            self (FileStorage): the current instance
        """
        d = {}
        for key, value in FileStorage.__objects.items():
            # The objects are converted to dictionaries
            d[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            # The dictionaries are dumped into a JSON file
            json.dump(d, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects (if it exists).
        Args:
            self (FileStorage): the current instance
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                d = json.load(f)
            for key, value in d.items():
                # The class name is extracted from the dictionary
                cls_name = value["__class__"]
                # The class is evaluated from its name
                cls = eval(cls_name)
                # A new object is created and added to the dictionary
                FileStorage.__objects[key] = cls(**value)
        # If the file does not exist, nothing happens
        except FileNotFoundError:
            # see the other comment
            return
