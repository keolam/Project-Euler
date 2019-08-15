'''
The decimal number, 585 = 1001001001(sub 2) (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''


def palindromic_sum(limit):
	ans = sum(i for i in range(limit) if binary_palindrome(i))
	return str(ans)


def binary_palindrome(n):
	s = str(n)
	if s != s[ : : -1]:
		return False
	t = bin(n)[2 : ]
	return t == t[ : : -1]

print(palindromic_sum(1000000))

#prints: 872187











