"""adapted mymath module
Claudia Pastellides
15 April 2014"""

def get_integer(y):
        if y=="n":
                n = input ("Enter n:\n") # if n is a string then repeat input unti digit is given
                while not n.isdigit ():
                        n = input ("Enter n:\n")
                n = eval (n)  
                return n #NB to return values to be reused
        else:
                k = input ("Enter k:\n")
                while not k.isdigit ():
                        k = input ("Enter k:\n")
                k = eval (k) 
                return k
        
def calc_factorial(x):
        factorial=1
        for i in range (1, x+1): #factorial is 4!= 1x2x3x4, hence why we start at 1 and end at x+1 (dont include x+1)
                factorial*= i    
        return factorial

