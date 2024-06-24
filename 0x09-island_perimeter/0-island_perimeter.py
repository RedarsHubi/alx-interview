#!/usr/bin/python3
"""Island Problem"""

def island_perimeter(grid):
    """Solution"""
    res = 0

    for row in grid:
        for cell in row:
            if cell == 1:
                res += 2
    if res != 0:
        res += 2
    
    return res
