#Shivam Ragoonaden
#Functions for factorial calculation

def get_integer(s): 
    #Get Integer
    if s == "n":
        n = input ("Enter n:\n")
        while not n.isdigit ():  #Test if input is digit, will prompt the user indefinitely until clause is met
            n = input ("Enter n:\n")
        n = eval (n)  
        return n  #return the integer
    
    if s == "k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)
        return k  
    
def calc_factorial(n):
    #Get Factorial
    nfactorial = 1
    for i in range(1, n+1):
        nfactorial *= i
    return nfactorial  #return the value of the factorial calculated