"""Question3 Assignmengt 5
Yaseen Sulliman
16 April 2014"""

# Function for obtaining input for integer
def get_integer(value):
    value1 = input ("Enter "+value+":\n")
    while not value1.isdigit ():
        value1 = input ("Enter "+value+":\n")
    value = eval (value1)
    return value

# function to calculating factorial for permutations
def calc_factorial(value):
    p = 1
    for i in range (1, value+1):
        p *= i
    return p