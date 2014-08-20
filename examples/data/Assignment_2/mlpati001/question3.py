#program that calculates the value of PI and then computes and displays the area of a circle with radius entered by the user
#ATISANG MOLAPO
#STUDENT NUMBER:MLPATI001
import math

def main():
    x=math.sqrt(2)
    r=2/x
    pi=2*r
    
    while r!=1:
        x=math.sqrt(2+x)
        r=2/x
        pi=pi*r
    print("Approximation of pi:", round(pi,3))
    
    rad=eval(input("Enter the radius:\n"))
    
    if rad>=0:
        area=pi*(rad**2)   #calculate's the area
        area=round(area,3)
        print("Area:", area)
        
main()