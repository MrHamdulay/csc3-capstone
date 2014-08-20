import math

#get integers from user input
def get_integer(n):
    if(n=="n"):
        n = input("Enter n:\n")
        while(eval(n)<0 and not (str(n)).isdigit()):
            n = input ("Enter n:\n")
        return eval(n)
    else:
        k = eval(input ("Enter k:\n"))
        return k


# calculate factorial
def calc_factorial(n):
    n = n
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
       
    return nfactorial
    