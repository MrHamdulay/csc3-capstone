"""functions to calculate number of k-permutations of n items
peter m muriuki"""

#input intergers
def get_integer (x):
    n= input ("Enter"+" "+x+":\n")
    while not n.isdigit ():
        n=input ("Enter"+" "+x+":\n")
    return int(n)

def calc_factorial (f):
    nfactorial=1
    for i in range (1, f+1):
        nfactorial *= i  
    return nfactorial
