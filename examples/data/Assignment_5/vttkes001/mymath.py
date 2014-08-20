"""Math Function utiliser
Keshin Vittee
16 April 2014"""

def get_integer(n):
    a = n
    print("Enter ",a,":",sep="")
    n = input ("")
    while not n.isdigit ():
        print("Enter ",a,":",sep="")
        n = input ("")
    return eval (n) 

def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial
   