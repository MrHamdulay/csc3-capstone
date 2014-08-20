# program with the two required functions to calculate the number of k-permutations of n-items
# khadeejah omar
# 15 april 2014

# gets value of n and k
def get_integer(x) :
    
    if x == "n" :
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)
        return n
        
    if x == "k" :
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)
        return k

# calculates factorial
def calc_factorial(n) :
    
    y = 1
    while y == 1 :
        nfactorial = 1
        for i in range (1, n+1) : 
            nfactorial *= i
            y -= 1
        return nfactorial
    
    z = 1
    while z == 1:
        nkfactorial = 1
        for i in range (1, n-k+1) :
            nkfactorial *= i
            z -= 1
        return nkfactorial