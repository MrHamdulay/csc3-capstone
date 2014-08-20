#Mbongeni Mazibuko
#MZBMBO002
#Assignment 5

def get_integer(s):
    if s=='n':
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        return eval (n)
        
    if s=='k':
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        return eval (k)        
    
def calc_factorial(num):
    nfactorial = 1
    for i in range (1, num+1):
        nfactorial *= i
    return nfactorial