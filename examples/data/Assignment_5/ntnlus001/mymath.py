"""permutation
DR Luci Ntanjana (actuary)
16 april 2014"""

def get_integer(a):
    if a=="n":
        n=input("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n) 
        return n
        
    if a=="k":
        k=input("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k) 
        return k
def calc_factorial(number):
    nfactorial = 1
    for i in range (1, number+1):
        nfactorial *= i
    return nfactorial
    


    
        

