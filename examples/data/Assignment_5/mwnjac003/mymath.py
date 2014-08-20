# modules to get input and calculate factorial
# by Jacob Mwanza
# 16/04/2014

# get an input    
def get_integer(s):
    n = input ("Enter " + s + ":\n")
    while not n.isdigit ():
        n = input ("Enter "+ s +":\n")
    n = eval (n)     
    return n
    

# calculate the factorial of an input
def calc_factorial(s):
    r = 1
    for i in range (1,s+1):
        r *=i
    return r
          