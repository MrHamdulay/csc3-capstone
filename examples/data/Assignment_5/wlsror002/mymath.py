def get_integer(letter):
    x='Enter '+letter+':\n'
    integer = input (x)
     
    while not integer.isdigit ():
        integer = input (x)
    integer = eval (integer)  
    return integer
    
def calc_factorial(x):
    factorial = 1
    for i in range (1, x+1):
        factorial *= i  
    return factorial