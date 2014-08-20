def calc_factorial(a):
    factorial = 1
    for i in range (1, a+1):
        factorial *= i
    return factorial
def get_integer (b):
    if b == "n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        return eval (n)  
    if b == "k":
        n = input ("Enter k:\n")
        while not n.isdigit ():
            n = input ("Enter k:\n")
        return eval (n)  
    