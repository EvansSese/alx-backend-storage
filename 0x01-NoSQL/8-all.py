#!/usr/bin/env python3
"""MongoDB using python"""


def list_all(mongo_collection):
    """List all docs in a collection"""
    docs = list(mongo_collection.find())

    return docs

