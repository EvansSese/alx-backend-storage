#!/usr/bin/env python3
"""MongoDB using python"""


def insert_school(mongo_collection, **kwargs):
    """Insert new document into a collection based on kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
