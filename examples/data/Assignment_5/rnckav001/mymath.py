#ass.5 Q3 n-k permutations
#Kavir Ranchod rnckav001
#16/04/2014

def get_integer(s):
    z="Enter "+str(s)+":\n"
    y=input(z)
    while not y.isdigit ():
        y=input (a)
    s=eval (y)   
    return s

def calc_factorial(s):
    fact=1
    for i in range (1,s+1):
        fact*= i
    return fact