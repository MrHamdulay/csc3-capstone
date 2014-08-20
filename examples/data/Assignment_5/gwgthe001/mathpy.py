#Thembekani Gwegwana
#April 2014
def get_integer(i):
    n = input ("Enter ", i,":\n")
    while not n.isdigit ():
        n = input ("Enter ", i,":\n")
    n = eval (n)
    return n
    
def calc_factorial(n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i  
    return nfactorial
#def math():
    #n=n.get_integer(n)
    #k=n.get_integer(k)
math()