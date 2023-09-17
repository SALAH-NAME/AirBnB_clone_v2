#!/usr/bin/python3
"""
This module defines the BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.
        Args:
            self (BaseModel): the current instance
            args (any): not used here
            kwargs (dict): dictionary of key/value pairs attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # Convert created_at and updated_at to datetime objects
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    # Set attribute on instance
                    setattr(self, key, value)
        else:
            # Assign a unique id to the instance using uuid.uuid4()
            self.id = str(uuid.uuid4())
            # Assign the current date to the created_at and updated_at atributs
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the instance.
        Args:
            self (BaseModel): the current instance
        Returns:
            str: a string representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        Args:
            self (BaseModel): the current instance
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance.
        Args:
            self (BaseModel): the current instance
        Returns:
            dict: a dictionary representation of the instance
        """
        # Create a copy of the instance's __dict__ attribute
        d = self.__dict__.copy()
        # Convert the created_at and updated_at attributes to ISO format strs
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        # Add the class name to the dictionary under the key '__class__'
        d["__class__"] = self.__class__.__name__
        return d
