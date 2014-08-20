"""Program to define factorial
Sbonelo Mntungwa
17 April 2014"""

def get_integer(x):
    while x == "n":
        n = input("Enter n:\n")
        while not n.isdigit():
            n = input("Enter n:\n")
        n = eval(n)
        return n
    k = input("Enter k:\n")
    while not k.isdigit():
        k = input("Enter k:\n")
    k = eval(k)
    return k
    
        
def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial

def calc_factorial(y):
    nkfactorial = 1
    for i in range (1, y+1):
        nkfactorial *= i
    return nkfactorial