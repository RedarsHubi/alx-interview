#!/usr/bin/python3
"""
solutiob
"""


def makeChange(coins, total):
    """
    determine the fewest n of coins
    """
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    change = 0
    for coin in coins:
        while total - coin >= 0:
            change += 1
            total -= coin
    return change if total == 0 else -1
