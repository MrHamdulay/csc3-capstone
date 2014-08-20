# question3.py

import math 

def main():
    pi = 2 
    a = 2
    x = math.sqrt(2)
    
    while x!=2:                     #Indefinite Loop while denominator<2
        f = a/x
        pi = pi*f        
        x = math.sqrt(2+x)
        
     
    print ("Approximation of pi:", (round((pi),3)))
    radius = eval(input("Enter the radius:\n"))
    area = (radius**2)*pi
    area = round(area,3) 
    print("Area:",area)
    
    
main() 
        
    