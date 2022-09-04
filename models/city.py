#!/usr/bin/env python3
"""City Class.

This module contains a class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines the blueprint of the City.

    Attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
