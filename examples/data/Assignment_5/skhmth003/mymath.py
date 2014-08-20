# Function to get input and return a value which can be parsed by calc_factorial() when called
def get_integer(x):
    a=x
    while not a.isdigit ():
        a = input ("Enter "+ x +":\n")
    a = eval (a)    
    return (a)

def calc_factorial(x_int):
    """function to calculate the factorial of a number"""
    fact = 1
    for num in range(1,x_int+1):
        fact *= num
    return fact