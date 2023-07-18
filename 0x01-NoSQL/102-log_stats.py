#!/usr/bin/env python3
"""
Log stats - new version
"""


from pymongo import MongoClient


def nginx_stats():
    """
    provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://localhost:27017')
    logs = client.logs.nginx

    num_docs = logs.count_documents({})
    print(f"{num_docs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        num_method = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {num_method}")
    check = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{check} status check")

    print("IPs:")
    top_ips = logs.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for ip in top_ips:
        count = ip.get("count")
        ip_id = ip.get("_id")
        print(f"\t{ip_id}: {count}")


if __name__ == "__main__":
    nginx_stats()
