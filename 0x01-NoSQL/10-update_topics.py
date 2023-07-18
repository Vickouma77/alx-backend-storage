#!/usr/bin/env python3
"""
changes all topics of a school document based on the name
"""


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    """
    if not mongo_collection:
        return None
    return mongo_collection.update_many({
        "name": name},
        {"$set": {"topics": topics}
         }).modified_count
