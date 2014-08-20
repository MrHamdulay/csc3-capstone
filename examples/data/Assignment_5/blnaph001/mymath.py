#calculate permutations
#aphiwe baleni
#16 april 2014
"""compute the factorial"""
def calc_factorial (n):
    fact=n
    for i in range(1,n):
        fact*=(n-i)
    return fact
def  get_integer (x):
    if x=='n':
        n=eval(input('Enter n:\n'))
        return n 
    
    if x=='k':
        k=eval(input('Enter k:\n'))
        return k     
