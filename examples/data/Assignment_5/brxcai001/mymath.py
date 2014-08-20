#Program that calculates the number of k-permutations of n items.
#BRXCAI001
#16 April 2014

#combine two functions.

#create first function by using the already created program "combine.py".

def get_integer(integer):
    if integer == 'n':
        n = input ("Enter n:\n")
        while not n.isdigit():
            n= input ("Enter n:\n")
        n= eval (n)
        return n
    else:
        k = input ("Enter k:\n")
        while not k.isdigit():
            k= input ("Enter n:\n")
        k= eval(k)
        return k
    
#create second function by using the already created program "question3.py".
    
def calc_factorial(z):
    factorial = 1
    for i in range (1, z+1):
        factorial *= i
    return factorial
