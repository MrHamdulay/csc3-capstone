#Rorisang Moseli
#April 2014
#Functions for question 3

def get_integer (n):
    x = input("Enter "+n+":\n")
    while not x.isdigit ():
        x=input("Enter "+n+":\n")
    n = eval(x)
    return n

def calc_factorial (n):
    nfactorial=1
    for i in range(n,0,-1):
        nfactorial*=i
    return nfactorial
