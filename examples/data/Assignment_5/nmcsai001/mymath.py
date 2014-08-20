"""Saijil Nemchund
NMCSAI001
17/4/2014"""

def calc_factorial(x): #function to calculate factorial
    factorial = 1
    for j in range (1, x+1):
        factorial *= j
    return factorial

def get_integer(x):#function to get integer 
    t = input ("Enter "+x+":\n")
    while not t.isdigit ():
        t =input ("Enter "+x+":\n")
    t= eval(t)
    return t
