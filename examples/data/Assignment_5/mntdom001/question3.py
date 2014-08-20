# calculate number of k-permutations of n items
# bhavana harrilal
# 10 April 2014


def get_integer(s):
    """ this function will prompt the user to enter a number. The number
    will either be the number of items to choose from, n, or the number of 
    items that are chosen, k"""
    
    # this will happen if we are asking the user for the number of items, n,
    # which they can choose
    if s == "n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)
        return n
      
    # this will happen if we are asking the user for the number of items, k, 
    # that are choosen
    elif s =="k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)   
        return k
    
def calc_factorial(x):
    """ this funtion will determine the factorial of the parameter x and 
    return the answer of the factorial of x"""
    
    # initialize the factorial to 1 
    nfactorial = 1
    
    # this loop will determine the factorial of x
    for i in range (1, x+1):
        nfactorial *= i    
    return nfactorial


def main ():
    n = get_integer ("n")
    k = get_integer ("k")
    nfactorial = calc_factorial (n)
    nkfactorial = calc_factorial (n-k)
    print ("Number of permutations:", nfactorial // nkfactorial)

if __name__ == "__main__":
    main()
