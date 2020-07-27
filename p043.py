'''

The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather 
interesting sub-string divisibility property.

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

import itertools


def compute():
	ans = sum(int("".join(map(str, num)))
		for num in itertools.permutations(list(range(10)))
		if is_substring_divisible(num))
	return str(ans)


DIVISIBILITY_TESTS = [2, 3, 5, 7, 11, 13, 17]

def is_substring_divisible(num):
	return all((num[i + 1] * 100 + num[i + 2] * 10 + num[i + 3]) % p == 0
		for (i, p) in enumerate(DIVISIBILITY_TESTS))


if __name__ == "__main__":
	print(compute())