# finding permutations
# Sohail Tulsi TLSSOH001
# 15 April 2014


 # create module to get integer 
def get_integer(b):
    w = input( "Enter " + b + ":\n")
    while not w.isdigit ():                # if not a digit
        w = input( "Enter " + b + ":\n")
    w= eval(w)
    return w
        
# create module to calculate factorial        
def calc_factorial(m):
    nfactorial = 1
    for i in range (2, m+1):     
        nfactorial *= i
    return nfactorial
    