# import sys 
# sys.setrecursionlimit(10000)

def factorial(n):
    # asert case
    assert n >= 0 and int(n) == n, 'The number must be a positive integer.'
    # base condition
    if n in [0,1]:
        return 1
    else:
        # print(n)
        return n * factorial(n-1)

print(factorial(4))