#mymath
#Julian van Rebsurg
def get_integer (n):
    s = input ("Enter " + n + ":\n")
    while not s.isdigit ():
        s = input ("Enter " + n + ":\n")        
    s = eval(s)
    return s

def calc_factorial (n):
    factorial = 1
    for i in range (1, n+1):
        factorial *= i
    return factorial