#mymath
#Annika Brundyn
#16/04/2014

def get_integer(x):
    if x == "n":
        n = input ("Enter n: \n")
        while not n.isdigit():
            n = input ("Enter n: \n")
        return eval(n)
    
    else:
        k = input ("Enter k: \n")
        while not k.isdigit():
            k = input ("Enter k: \n")
        return eval(k)
        
def calc_factorial(a):
    nfactorial = 1
    for i in range (1, a+1):
        nfactorial *= i
    return nfactorial
