'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

'''

import itertools, sympy

def sum_of_trunc_primes():
	ans = sum(itertools.islice(filter(is_truncatable_prime, itertools.count(10)), 11))
	return str(ans)


def is_truncatable_prime(n):
	# Test if left-truncatable
	i = 10
	while i <= n:
		if not sympy.isprime(n % i):
			return False
		i *= 10
	
	# Test if right-truncatable
	while n > 0:
		if not sympy.isprime(n):
			return False
		n //= 10
	return True

print(sum_of_trunc_primes())



#prints: 748317















