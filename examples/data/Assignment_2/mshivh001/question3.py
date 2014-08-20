#program for calculating the value of PI and then computes and displays the area of a circle with radius entered by the user
#MSHIVH001
#Maisha Ivha
#14/03/2014
import math

def main():
    x=math.sqrt(2)
    y=2/x
    pi=2*y
    
    while y!=1:
        x=math.sqrt(2+x)
        y=2/x
        pi=pi*y
    print("Approximation of pi:", round(pi,3))
    
    rad=eval(input("Enter the radius:\n"))
    
    if rad>=0:
        area=pi*(rad**2)   #calculate's the area
        area=round(area,3)
        print("Area:", area)
        
main()