# This Python file uses the following encoding: utf-8
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def max_palindrome():
    palindromes = (i * j
        for i in reversed(range(100, 1000))
        for j in reversed(range(100, 1000))
        if str(i * j) == str(i * j)[: : -1]
        )
    return max(palindromes)

if __name__ == "__main__":
	print(max_palindrome()) 

# prints: 906609





