"""this program uses two function to get an interger and calculates the factorial
of the interger
quincy cele
15 april 2014"""

def get_integer(value):
    a= input("Enter "+value+":\n")
    while not a.isdigit ():
        a = input ("Enter "+value+":\n")
    a= eval(a)
    return a
    
def calc_factorial(value):
    nkfactorial = 1
    for i in range (1, value+1):
        nkfactorial *=i
    return nkfactorial
        
        
        
    
    
    

    