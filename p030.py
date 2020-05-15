# This Python file uses the following encoding: utf-8
'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

'''
import sys
if sys.version_info.major == 2:
    range = xrange

def sum_of_nth_power_numbers(exponent):
    ans = sum(i for i in range(2, exponent*9**exponent) if i == fifth_power_digit_sum(i, exponent))
    return str(ans)

def fifth_power_digit_sum(n, exp):
    return sum(int(c)**exp for c in str(n))

if __name__ == "__main__":
  print(sum_of_nth_power_numbers(5))


#prints: 443839





