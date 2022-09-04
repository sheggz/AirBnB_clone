#!/usr/bin/env python3
"""State Class.

This module contains a class that inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Defines the blueprint of the State.

    Attributes:
        name: string - empty string
    """
    name = ""
