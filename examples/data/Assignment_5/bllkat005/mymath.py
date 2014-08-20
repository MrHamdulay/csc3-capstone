# Kate Bell
# BLLKAT005
# 16 April 2014

def get_N ():
    """Prompt user to enter digit n"""
    n = input ("Enter n:\n")
    while not n.isdigit ():
       n = input ("Enter n:\n")
    n = eval (n)  
    return n

def get_K ():
    """Prompt user to enter digit k"""
    k = input ("Enter k:\n")
    while not k.isdigit ():
       k = input ("Enter k:\n")
    k = eval (k)  
    return k

def calc_factorial1 (n):
    """Calculate the factorial of a number n"""
    nfactorial = 1
    for i in range (1, n+1):
       nfactorial *= i  
    return nfactorial

def calc_factorial2 (n,k):
    """Calculates the number of k-permutations of n items"""
    nkfactorial = 1
    for i in range (1, n-k+1):
       nkfactorial *= i    
    return nkfactorial
