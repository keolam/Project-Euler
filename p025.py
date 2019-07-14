import itertools

def fib_term_digits(num_len):
    prev = 1
    cur = 0
    for i in itertools.count():
        if len(str(cur)) > num_len:
            raise RuntimeError("Does Not Exist")
        elif len(str(cur)) == num_len:
            return str(i)		
        prev, cur = cur, prev + cur

print(fib_term_digits(1000))

#prints: 4782





