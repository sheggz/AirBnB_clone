#!/usr/bin/env python3
"""Amenity Class.

This module contains a class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines the blueprint of the Amenity.

    Attributes:
        name: string - empty string
    """
    name = ""
