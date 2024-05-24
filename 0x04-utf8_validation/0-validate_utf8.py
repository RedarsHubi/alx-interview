#!/usr/bin/python3
"""
Module for utf 8 validation
"""


def validUTF8(data):
    """
    Determines if UTF-8 encoding valid.
    """
    def leading_ones(byte):
        count = 0
        for i in range(7, -1, -1):
            if (byte >> i) & 1:
                count += 1
            else:
                break
        return count

    i = 0
    while i < len(data):
        num = data[i]
        if num < 0 or num > 127:
            return False

        leading = leading_ones(num)
        if leading == 0:
            i += 1
            continue

        if leading == 1 or leading > 4:
            return False
        for j in range(1, leading):
            if i + j >= len(data) or leading(data[i + j]) != 1:
                return False
        i += leading
    return True
