# This Python file uses the following encoding: utf-8
"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

def compute_diff(num):
    sq_of_sum = sum(i for i in range(1, num + 1))**2
    sum_of_sq = sum(i**2 for i in range(1, num + 1))
    return str(sq_of_sum - sum_of_sq)

if __name__ == "__main__":
	print(compute_diff(100))

#prints:  25164150






