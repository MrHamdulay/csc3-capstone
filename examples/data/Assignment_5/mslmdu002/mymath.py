'''This Program calculates the number of k-permutations of n items
Mduduzi Masilela
17 April 2014'''
def get_integer (i):
    """get the value from the user """
    if i=='n': #check for n
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)
        x=n
    
    elif i=='k': #get the value of k
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)
        x=k
    return x

def calc_factorial (n_0r_n_k):
    """Calculate the factorials of n and n-k"""
    factorialvalue = 1
    for i in range (1, n_0r_n_k+1):
        factorialvalue *= i  
    return factorialvalue 