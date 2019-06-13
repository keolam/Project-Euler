"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import numpy as np

def largets_prime(n):
	while True:
		p = smallest_prime(n)
		if p < n:
			n //= p
		else:
			return str(n)

def smallest_prime(n):
	assert n >= 2
	sqrt = np.sqrt(n).astype(np.int64)
	for i in range(2, sqrt(n) + 1):
		if n % i == 0:
			return i
	return n


print(largest_prime(600851475143))  # prints 6857