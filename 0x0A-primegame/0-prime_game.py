#!/usr/bin/python3
"""
Prime Game module.

This module provides a solution to the Prime Game where two players, Maria and
Ben,take turns picking prime numbers and their multiples from a set of
consecutive integers.
"""

from typing import List, Optional


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n: int) -> List[bool]:
    """
    Generate a list indicating prime numbers up to n using the Sieve of
    Eratosthenes.

    Args:
        n (int): The upper bound of the sieve.

    Returns:
        List[bool]: List where True indicates a prime number.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return sieve


def isWinner(x: int, nums: List[int]) -> Optional[str]:
    """
    Determine the winner of the Prime Game.

    Args:
        x (int): The number of rounds.
        nums (List[int]): List of integers representing the rounds.

    Returns:
        Optional[str]: The name of the player who won the most rounds
        (either 'Maria' or 'Ben').
                       Return None if the winner cannot be determined.
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_count = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
