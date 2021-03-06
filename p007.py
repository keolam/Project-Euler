# This Python file uses the following encoding: utf-8
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

"""

import sympy
import itertools

def nth_prime(maximum):
    
    prime_obj = filter(sympy.isprime, itertools.count(2))
    iter_obj = next(itertools.islice(prime_obj, maximum - 1, None))
    return str(iter_obj)

if __name__ == "__main__":
	print(nth_prime(10001))

#prints: 104743




