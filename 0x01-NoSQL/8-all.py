#!/usr/bin/env python3
"""
list all documents in python
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    list all documents in python
    """

    if not mongo_collection:
        return []
    return mongo_collection.find()
