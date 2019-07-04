'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import math

def sum_of_factorial_digits(num):
    facto = math.factorial(num)
    sum_of_digits = sum(int(digit) for digit in str(facto))
    return str(sum_of_digits)

print(sum_of_factorial_digits(100))

#prints: 648




