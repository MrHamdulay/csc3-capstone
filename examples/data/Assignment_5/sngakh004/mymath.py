#Akhil Singh
#13 April 2014
#Assignment 5
#Question 3




def get_integer(x):
    n = input("Enter "+x+":\n")
    while not n.isdigit ():
        n = input("Enter "+x+":\n")
    n = eval(n)
    return n

def calc_factorial(k):
    nfactorial = 1
    for i in range (1,k+1):
        nfactorial *= i
    return nfactorial   
    

        
        