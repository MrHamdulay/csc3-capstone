#Question 3
#Adam Rosendorff-RSNADA001
#15/04/2014

def  get_integer(t):
    out = 0
    if t == 'n':
        n = input ("Enter n:\n")
        while not n.isdigit ():
           n = input ("Enter n:\n")
        out = eval (n)
    elif t == 'k':
        k = input ("Enter k:\n")
        while not k.isdigit ():
           k = input ("Enter k:\n")
        out = eval (k)
    return out

def calc_factorial(t):
    factorial = 1
    for i in range (1, t+1):
        factorial *= i
    return factorial
