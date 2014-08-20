"""Program dealing with permutations
Thiloshni Moodley(MDLTHI019)
15 April 2014"""

def get_integer(x): 
    if x == "n":
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)  
        return n
    
    if x == "k":
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)
        return k
    
def calc_factorial(n):
    #Getting Factorial
    nfactorial = 1
    for i in range(1, n+1):
        nfactorial *= i
    return nfactorial