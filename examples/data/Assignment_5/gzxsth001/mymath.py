def get_integer (x):
    n= input ("Enter"+" "+x+":\n")
    while not n.isdigit ():
        n=input ("Enter"+" "+x+":\n")
    return int(n)

def calc_factorial (o):
    nfactorial=1
    for i in range (1, o+1):
        nfactorial *= i  
    return nfactorial
