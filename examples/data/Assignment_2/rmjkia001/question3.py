import math
def aproxPi():
    denom=math.sqrt(2)
    ans=2/denom
    pi=2*ans
    while ans!=1:        
        denom=math.sqrt(2+denom)
        ans=2/denom
        pi*=ans    
    print("Approximation of pi:",round(pi,3))
    return pi
def calcArea(pi):
    rad= eval(input("Enter the radius: \n"))
    area = pi*rad**2     
    print("Area:",round(area,3))
if __name__ == "__main__":
    
    calcArea( aproxPi())
    
         
         
         
         
         
         
         
         
         
         
         
         #make a variable= sqrt of 2 put it in a while loop. Add 2 and sqrt it each time until the variable =2
         #use a variable to store the current denominator at any point in timetry to figure out how to convert the denominator from one term to the denominator of the next term