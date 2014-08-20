'''calculates k-permutations of n items
Author:Raees Eland
Date:15 April 2014'''

'''prompts the user for inputs'''
def get_integer(n):
    if n=='n':
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n=eval(n)
    elif n=='k':
        n = input ("Enter k:\n")
        while not n.isdigit ():
            n = input ("Enter k:\n")
        n = eval (n) 
    return n
''' calculates k-permutations of n items from users inputs'''       
def calc_factorial (s):
    nfactorial = 1
    for i in range (1,s+1):
        nfactorial *= i
    return nfactorial
