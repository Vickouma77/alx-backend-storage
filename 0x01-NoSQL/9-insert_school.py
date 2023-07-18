#!/usr/bin/env python3
"""
insert a document in Python
"""


from pymongo import mongo_client


def insert_school(mongo_collection, **kwargs):
    """
    insert a document in python
    """
    if not mongo_collection:
        return None
    return mongo_collection.insert_one(kwargs).inserted_id
