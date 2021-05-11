#!/usr/bin/python3
"""lockedclass"""


class LockedClass():
    """class doesnt allow dynamic attributes except first_name"""

    __slots__ = ['first_name']

    def __init__(self):
        """init method"""
