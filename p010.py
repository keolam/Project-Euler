# This Python file uses the following encoding: utf-8
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

from sympy.ntheory import isprime

def sum_of_primes(limit):
  nums = list(range(1, limit))
  result = list(filter(lambda x: isprime(x), nums))
  
  return sum(result)

if __name__ == "__main__":
  print(sum_of_primes(2000000))

#prints: 142913828922
