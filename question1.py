# step 1 : Recursive Case 
def sum_of_digits(n):
    # Step 3 : Unintentinal case - The Constant
    assert n >= 0 and int(n) == n, 'Enter a positive number.'
    
    # Step 2 : Base Case - the stop of criteration
    if  n == 0:
        return 0
    else: 
        return int(n%10) + sum_of_digits(int(n/10))

# add all the numbers
print(sum_of_digits(1234))