
def get_integer(n):
    no = input ("Enter " + n + ":\n")
    while not no.isdigit ():
        no = input ("Enter " + n + ":\n")
    no = eval (no)  
    return no
    
def calc_factorial(n):
    x = 1
    for i in range (1, n+1):
        x *= i
    return x