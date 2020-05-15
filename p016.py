# This Python file uses the following encoding: utf-8
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

def power_digit_sum(base, exponent):
    return sum(int(n) for n in str(base**exponent))

if __name__ == "__main__":
  print(power_digit_sum(2,1000))

#prints: 1366




