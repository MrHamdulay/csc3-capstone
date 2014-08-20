#program to find values for permutations
#Stephanie Latchamanan (LTCSTE001)
#16 April 2014

def get_integer(val):
    if val=='n':
        n = input("Enter n:\n")              #input a valid numerical value for n
        while not n.isdigit():
            n= input("Enter n:\n")
        return int(eval(n))
    elif val=='k':                           #input a valid numerical value for k
        k = input("Enter k:\n")
        while not k.isdigit():
            k= input("Enter k:\n")
        return int(eval(k)) 

def calc_factorial(fac):                     #calculate factorial of fac
    fac_n = 1
    for j in range (1, int(fac)+1):
        fac_n *= j
    return fac_n