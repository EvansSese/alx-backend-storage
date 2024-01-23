#!/usr/bin/env python3
"""MongoDB operations"""


def schools_by_topic(mongo_collection, topic):
    """Find schools that teach certain topics"""
    school_list_with_topic = list(mongo_collection.find({"topics": topic}))
    return school_list_with_topic
