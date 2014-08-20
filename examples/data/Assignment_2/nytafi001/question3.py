import math

def AreaCircle():
    
    pi = 2
    
    x = math.sqrt(2)
    
    nextterm = 2
    
    while (nextterm != 1): # This calculates an approximate value of pi using a given formula
        
        nextterm = 2/x
        
        pi *= nextterm # Is the same as pi = pi * nextterm
        
        x = math.sqrt(2 + x)
        
    
    print("Approximation of pi:", round(pi,3)) # This prints approximate value of pi using a rounded off figure
    
    
    
    radius = eval(input("Enter the radius:\n"))
    
    area = pi * radius**2 # This calulates the area of a given circle using pi calculated above
    
    print("Area:", round(area,3)) # I only round off figures when I'm printing, otherwise, the full values remain unrounded elswhere to keep accuracy


AreaCircle()