#!/usr/bin/env python3
"""MongoDB Operations using python"""
from pymongo import MongoClient


def stats_for_nginx():
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    number_of_logs = nginx_collection.count_documents({})
    print(f'{number_of_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')


if __name__ == "__main__":
    stats_for_nginx()
