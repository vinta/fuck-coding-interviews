# coding: utf-8
import random


PRIME = 109345121
SCALE = 1 + random.randrange(PRIME - 1)
SHIFT = random.randrange(PRIME)


def mad(hash_code, array_size):
    """
    It is common to view a hash function, h(k), as consisting of two parts:
    1. A hash code that maps a key k to an integer.
    2. A compression function that maps the hash code to an index within [0, N − 1], for a bucket array.

    We use Python's built-in hash() to produce hash code for key,
    and a randomized Multiply-Add-and-Divide (MAD) formula as compression function:

    ((hash_code * scale + shift) mod P) mod N

    where N is the size of the bucket array,
    P is a prime number larger than N,
    and scale and shift are random integers from the [0, p – 1], with scale > 0.
    """
    return ((hash_code * SCALE + SHIFT) % PRIME) % array_size
