"""returns numbers and factorial
Adam Kaliski
CSC1015 Assignment 5"""
def get_integer(n):
    if n=='n':
        num = input ("Enter n:\n")
        while not num.isdigit ():
            num = input ("Enter n:\n")
        num = eval (num)      
        return num 
    if n=='k':
        num = input ("Enter k:\n")
        while not num.isdigit ():
            num = input ("Enter k:\n")
        num = eval (num)      
        return num

def calc_factorial (n):
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i   
    return nfactorial