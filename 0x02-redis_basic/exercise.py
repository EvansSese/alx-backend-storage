#!/usr/bin/env python3
"""Redis basics"""
import uuid
import redis
from typing import Union


class Cache:
    """Cache class for Redis"""
    def __init__(self):
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
