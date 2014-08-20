""" Re-use adapt code
David Fransch
15-04-2014"""

def get_integer(var):
    
        if var == "n":
                n = input ("Enter n:\n")
                
                while not n.isdigit ():
                        n = input ("Enter n:\n")         
                n = eval (n)
                return n
        else:
                k = input ("Enter k:\n")
                while not k.isdigit ():
                    k = input ("Enter k:\n")
                k = eval (k)
                return k
    
def calc_factorial(input):
    nfactorial = 1
    for i in range (1, input+1):
       nfactorial *= i
    return nfactorial

    
    