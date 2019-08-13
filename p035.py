'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''


import sympy

def circular_prime_qty(limit):
  bool_prime_list = []
  for i in range(limit):
    bool_prime_list.append(sympy.isprime(i))

  def is_circular_prime(n):
    s = str(n)
    return all(bool_prime_list[int(s[i : ] + s[ : i])] for i in range(len(s)))
	
  ans = sum(1
    for i in range(len(bool_prime_list))
    if is_circular_prime(i))
  return str(ans)

print(circular_prime_qty(1000000))

#prints: 55











