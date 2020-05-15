# This Python file uses the following encoding: utf-8
'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:


012   021   102   120   201   210


What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''

import itertools, sys

def lex_perm(target):
    new_list = list(range(10))
    temp = itertools.islice(itertools.permutations(new_list), target - 1, None)
    return "".join(str(x) for x in next(temp))


if __name__ == "__main__":
  print(lex_perm(1000000))

#prints: 2783915460





