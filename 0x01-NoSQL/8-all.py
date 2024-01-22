#!/usr/bin/env python3
"""MongoDB using python"""


def list_all(mongo_collection):
    """List all docs in a collection"""
    docs = mongo_collection.find()

    if docs.count() == 0:
        return []
    return docs
