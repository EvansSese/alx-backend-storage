#!/usr/bin/env python3
"""MondoDB using python"""


def update_topics(mongo_collection, name, topics):
    """Update topics of school document"""
    result = mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count > 0
