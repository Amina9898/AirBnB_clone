#!/usr/bin/python3
# models/review.py
"""Defines Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class"""
    place_id = ""
    user_id = ""
    text = ""
