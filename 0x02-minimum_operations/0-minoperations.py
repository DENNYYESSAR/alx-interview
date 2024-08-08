#!/usr/bin/python3
"""
Module for calculating the minimum number of operations needed to achieve n
'H' characters.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n
    'H' characters.

    :param n: The desired number of 'H' characters.
    :return: The minimum number of operations needed, or 0 if n is impossible
    to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
