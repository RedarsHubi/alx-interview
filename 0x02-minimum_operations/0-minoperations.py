#!/usr/bin/python3
"""
Module for calculating most efficient way to copy and paste
"""


def minOperations(n):
    """Returns minium num of operations"""
    store = 0
    value = 1
    if (n <= 1):
        return 0
    if (n % 2 == 0):
        while value < n:
            store += 2
            value = value * 2
            if (value == n):
                return store
            elif value * 2 > n:
                store += 1
                return store
    elif n % 3 == 0:
        while value < n:
            if value % 2 == 0:
                value += value // 2
                store += 1
            else:
                value *= 2
                store += 2
        return store
    elif not ((n % 2 == 0)) or not (n % 3 == 0):
        while value < n:
            store += 1
            value *= 2
        return store
    else:
        while value < n:
            store += 1
            value *= 2
        return store
