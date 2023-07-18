#!/usr/bin/env python3
"""
Where can I learn Python?
"""


from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    """
    if not mongo_collection:
        return None
    return mongo_collection.find({"topic": "topic"})
