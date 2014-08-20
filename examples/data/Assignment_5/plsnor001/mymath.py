#-------------------------------------------------------------------------------
# Name:        mymath
# Purpose:  calculate number of k-permutations of n items
# Author:      Pilusa
# Created:     15-04-2014
# Copyright:   (c) Pilusa 2014
#-------------------------------------------------------------------------------

def get_integer (a):    #get integer from user
    n = input ("Enter "+a+":\n")
    while not n.isdigit (): #checks if number is not string
        n = input ("Enter "+a+":\n")
    if n.isdigit():
        n = eval (n)
    return n #returns a "numeric" number

def calc_factorial (n):#calculate factorial
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial


