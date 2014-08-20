#question3
#Name: ShaheenKarodia
#Student Number: KRDSHA003
#Date: 2014-03-11

#Program to calculate pi, and then calculate the area
import math

def main():
    
    pi=2                                #initialize a
    denom=math.sqrt(2)                  #Initialise b
       
    while denom <2:                     #Condtion when loop must stop interating
        
        b=2/denom
        denom=math.sqrt(2+denom)
        
        pi=pi*b
        
    print("Approximation of pi:", round(pi, 3))
    
    r=eval(input("Enter the radius:\n"))
    
    area=pi*r**2
    print("Area:", round(area, 3))
        
  
    
main()
        