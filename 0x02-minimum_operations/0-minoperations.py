#!/usr/bin/python3
"""
Module for calculating most efficient way to copy and paste
"""


def minOperations(n):
    """Returns minimum num of operations"""
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
