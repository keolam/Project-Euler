'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''


def amicable_number_sum(n):

	divisorsum = [0] * n
	for i in range(1, len(divisorsum)):
		for j in range(i * 2, len(divisorsum), i):
			divisorsum[j] += i
	

	amicable_sum = 0
	for i in range(1, len(divisorsum)):
		j = divisorsum[i]
		if j != i and j < len(divisorsum) and divisorsum[j] == i:
			amicable_sum += i
	return amicable_sum


print(amicable_number_sum(10000))

#prints: 31626



