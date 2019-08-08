'''

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math, sys

def curious_number_sum():
    ans = sum(i for i in range(3, 10000000) if i == factorial_digit_sum(i))
    return str(ans)

def factorial_digit_sum(n):
    result = 0
    while n >= 10000:
        result += fact_digit_sum_leading_zeros[n % 10000]
        n //= 10000
        return result + fact_digit_sum[n]

fact_digit_sum = [sum(math.factorial(int(c)) for c in str(i)) for i in range(10000)]
fact_digit_sum_leading_zeros = [sum(math.factorial(int(c)) for c in str(i).zfill(4)) for i in range(10000)]

print(curious_number_sum())


#prints: 40730









