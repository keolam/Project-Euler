# This Python file uses the following encoding: utf-8
'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

'''

import math

def curious_product_denom():
    nmr = 1
    dnm = 1
    for d in range(10, 100):
        for n in range(10, d):
            n0 = n % 10
            n1 = n // 10
            d0 = d % 10
            d1 = d // 10
            if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
                nmr *= n
                dnm *= d
    return str(dnm // math.gcd(nmr, dnm))

if __name__ == "__main__":
  print(curious_product_denom())

# prints: 100






















