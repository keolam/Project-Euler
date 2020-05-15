# This Python file uses the following encoding: utf-8
import numpy as np

def pythag_triplet(target):
    #using brute-force, only half target needs to be searched as there are only two values being summed 
    half_val = int(target/2)
    for a in range(1, half_val):
        for b in range(1, half_val):
            c = np.sqrt(a**2 + b**2)

            if a + b + c == int(target):
                print(f"a: {a}, b: {b}, c: {c}")
                print(f"Product: {a*b*c}")
                return


if __name__ == "__main__":
	pythag_triplet(1000)

#prints: a: 200, b: 375, c: 425.0, Product: 31875000.0