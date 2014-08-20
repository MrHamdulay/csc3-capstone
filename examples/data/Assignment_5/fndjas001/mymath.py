"""Contains functions used for  calculating the number of k-permutations of n items
Jason Findlay
16/04/2014"""

def get_integer(a):
    if a=="n":
        n=input("Enter n:\n")
        while not n.isdigit():
           n = input ("Enter n:\n")
        n = eval (n)
        return(n)
    elif a=="k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
           k = input ("Enter k:\n")
        k = eval (k)
        return(k)

def calc_factorial(a):
    n=a
    afactorial = 1
    for i in range(1,n+1):
        afactorial*=i
    return(afactorial)

