def get_integer(n):
    
    ints = input("Enter " + n + ":\n")
    
    while not ints.isdigit ():
        ints = input("Enter " + n + ":\n")

    ints = eval(ints)

    return ints
        
        
def calc_factorial (n): 
    
    nfact1 = 1

    for i in range (1, n+1):
        nfact1 = nfact1 * i

    return nfact1