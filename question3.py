
# Recursion Case
def gcd(a, b):

    # Step 3 : Unintentinal Case
    assert int(a) == a and int(b) == b, 'Enter a positive integer number.'
     
    if a < 0 :
        a = -1 * a
    if b < 0:
        b = -1 * b

    # Step 2 : Base Condition Case
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(48, 1.8))