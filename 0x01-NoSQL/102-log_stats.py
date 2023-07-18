#!/usr/bin/env python3
"""
Log stats - new version
"""


from pymongo import MongoClient


def log_stats(mongo_collection, option=None):
    """
    provides some stats about Nginx logs stored in MongoDB
    """
    if option is None or not mongo_collection:
        return 0
    if option == "method":
        return mongo_collection.count_documents({"method": "GET"})
    if option == "path":
        return mongo_collection.count_documents(
            {"method": "GET", "path": "/status"}
        )
    return mongo_collection.count_documents({})
