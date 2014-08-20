import math

def Area_Circle() :
    
    pi = (2) * (2/math.sqrt(2)) # first two terms in pi calculation
    denominator = math.sqrt(2) # denominator of second term in pi calculation
    
    # pi calculation:
    while denominator != 2 :
        x = 2 + denominator
        y = math.sqrt(x)
        term = (2/y)
        pi = pi*term
        denominator = y
   
    print("Approximation of pi:", round(pi,3))
    radius = eval(input("Enter the radius:\n"))
    print("Area:", round(pi*(radius**2),3))    

Area_Circle()