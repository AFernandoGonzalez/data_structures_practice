# How ot calculate power of a number using recursion
# x^n = x*x*3(n..times)..*x

# Step 1 : Recursion Case - The Flow
def power(base, exp):

    # Step 3
    assert exp >= 0 and int(exp) == exp, 'The exponent must be an integer'


    # Step 2 : Base Condition
    if exp == 0:
        return 1
    if exp == 1:
        return base
    
    return base * power(base, exp-1)

print(power(2,-9))
