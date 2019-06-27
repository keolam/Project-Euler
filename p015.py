
'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

'''


from sympy import binomial

def lattice_path(n):
	return binomial(2*n, n)

print(lattice_path(20))

prints: #137846528820




