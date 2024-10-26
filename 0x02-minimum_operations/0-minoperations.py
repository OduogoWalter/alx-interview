#!/usr/bin/python3
"""
Module for calculating minimum operations needed to achieve n H characters
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in exactly n H
    characters in the file.

    Args:
        n (int): Target number of H characters

    Returns:
        int: Minimum number of operations needed. Returns 0 if n is impossible
             to achieve.
    """
    # If n is 1, we already have 'H', so no operations needed
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Continue until we've factored out all divisors
    while n > 1:
        # If divisor divides n evenly
        while n % divisor == 0:
            # Add the divisor to operations (Copy All + Paste operations)
            operations += divisor
            # Divide n by the divisor
            n //= divisor
        # Move to next potential divisor
        divisor += 1

        # Optimization: if divisor squared is greater than n,
        # and n is greater than 1, then n is prime
        if divisor * divisor > n and n > 1:
            operations += n
            break

    return operations
