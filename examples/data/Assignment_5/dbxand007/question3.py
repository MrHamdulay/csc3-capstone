"""Cherise Dube 
14 April 2014
Program to determine the number of k permutations of n items"""

#Gets the integer from the user and ensures that user enters a numerical value for both n and k 
def get_integer(i):
    if i=='n':
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval (n)  
        return n
        
    elif i=='k':
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval (k)
        return k

#Calculates the fatorial of a given number
def calc_factorial(factorial_value):
    factorial=1
    for i in range(1,factorial_value+1):
        factorial*= i
    return factorial

def main ():
    n = get_integer ("n")
    k = get_integer ("k")
    nfactorial = calc_factorial (n)
    nkfactorial = calc_factorial (n-k)
    print ("Number of permutations:", nfactorial // nkfactorial)

if __name__ == "__main__":
    main()

