#!/usr/bin/env python3
"""Redis basics"""
import uuid
from functools import wraps

import redis
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
    """Counts number of calls"""
    counts = {}

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Cache class for Redis"""

    @count_calls
    def __init__(self):
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
        str, bytes, int, float, None]:
        """get function"""
        data = self._redis.get(key)
        if data is not None:
            return fn(data) if fn else data
        return None

    def get_str(self, key: str) -> Union[str, None]:
        """get str function"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """get int function"""
        return self.get(key, fn=int)
