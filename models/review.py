#!/usr/bin/python3
"""
This is a Rewiew class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class that represents a review."""
    place_id = ""
    user_id = ""
    text = ""
