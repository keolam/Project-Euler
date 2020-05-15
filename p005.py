# This Python file uses the following encoding: utf-8
"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import functools as ft
import fractions

def lcm(a, b):
    return a * b // fractions.gcd(a, b)

def find_lcm(*args):
    return ft.reduce(lcm, args)


if __name__ == "__main__":
	print(find_lcm(*range(1, 20)))

# prints: 232792560






