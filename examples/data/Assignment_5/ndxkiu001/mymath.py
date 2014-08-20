#Kiuran Naidoo
#mymath.py
#Assignment 5
def get_integer(x):
    if x == "n":
        x = input ("Enter n: \n")
        while not x.isdigit():
            x = input ("Enter n: \n")
        x = eval(x)
        return x
    if x=="k":
        x = input ("Enter k: \n")
        while not x.isdigit():
            x = input ("Enter k: \n")
        x = eval (x)
        return x
        
def calc_factorial(x): #Calculate factorial
    nfactorial = 1
    for i in range (1, x+1):
        nfactorial *= i #Normally I would use a math function instead of a loop but I just used combine.py instead
    return nfactorial
