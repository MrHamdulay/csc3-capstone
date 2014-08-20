""" functions that calculate the factorial of a number
tafara mtutu
16 april 2014"""

def get_integer(text):
    while True:
        print("Enter ", text, ":", sep = "")
        val = input()
        if val.isdigit():
            break
    return eval(val)  

def calc_factorial(i):
    nfactorial = 1
    for i in range (1, i+1):
        nfactorial *= i 
    return nfactorial
        
