"""zikho godana
16 april 2014
program to define two functions to be called by question3.py program"""

def get_integer(p):
    s = input ("Enter "+str(p)+":\n")
    while not s.isdigit ():
        s = input ("Enter " + str(p)+":\n")
    s = eval (s)
    return s
    
def calc_factorial(x):
    sfactorial = 1
    for i in range (1, x+1):
        sfactorial *= i
    return sfactorial
    
       
    