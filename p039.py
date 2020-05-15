# This Python file uses the following encoding: utf-8
'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

'''

def max_sol(p):
  ans = max(range(1, p + 1), key=count_solutions)
  return str(ans)


def count_solutions(p):
  count = 0
  for a in range(1, p + 1):
    for b in range(a, (p - a) // 2 + 1):
      c = p - a - b  # c >= b
      if a * a + b * b == c * c:
        count += 1
  return count


if __name__ == "__main__":
	print(max_sol(1000))

#prints 840