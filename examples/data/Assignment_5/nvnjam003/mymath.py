def get_integer(n):
    string = "Enter " + n + ":\n"
    i = input (string)
    while not i.isdigit ():
        i = input (string)
    i = eval (i) 
    return i

def calc_factorial(n):
    factorial = 1
    for x in range (1, n+1):
        factorial *= x
    return factorial