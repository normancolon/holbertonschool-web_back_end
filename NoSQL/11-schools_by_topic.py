#!/usr/bin/env python3
""" Practicing pymongo """


def schools_by_topic(mongo_collection, topic):
    """
    Write a Python function that returns the
    list of school having a specific topic
    """
    return mongo_collection.find({'topics': topic})


if __name__ == '__main__':
    schools_by_topic(mongo_collection, topic)