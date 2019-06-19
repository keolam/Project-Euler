"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

"""

import sympy
import itertools

def nth_prime(max):
    
    prime_obj = filter(sympy.isprime, itertools.count(2))
    iter_obj = next(itertools.islice(prime_obj, max - 1, None))
    return str(iter_obj)

print(nth_prime(10001))

#prints: 104743




