

def fibonacci(n):
    # intentional case negatives or float
    assert n >= 0 and int(n) == n, "Enter a positive number."
    # base condition
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))
