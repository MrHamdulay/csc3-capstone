from math import *

def main():
    pi = 2
    denom = sqrt(2)
    
    while denom!=2 :
       
        pi*= 2 / denom
        denom = sqrt(2 +denom)
        
print("Approximation of pi:", round(pi,3))
rad = eval(input("Enter the radius:\n"))
Area= (pi*(rad)**2)
print("Area:", round(Area,3))

        
main()