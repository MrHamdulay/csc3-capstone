# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014


def get_integer (x):
    print("Enter", x, end="")
    print(":")
    n=input()
    
    while not n.isdigit ():
        print("Enter", x, end="")
        print(":")
        n=input()               
    n = eval (n) 
    return n 

   
    


def calc_factorial (n):
    fact = 1
    for i in range(2,n+1):
        fact*= i
    return fact


def calc_factorial (z):
    fact=1
    for i in range(2, (z) +1):
        fact *=i
    return fact
    