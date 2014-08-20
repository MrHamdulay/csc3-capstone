def get_integer(t):
    if t=="n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)
        return(n)
        
    elif t=="k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)
        return(k)
        
def calc_factorial(p):
    factorial = 1
    for i in range (1, p+1):
        factorial *= i
    return(factorial)
        