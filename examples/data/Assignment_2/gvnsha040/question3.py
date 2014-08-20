import math

sq = math.sqrt(2)
a=2/sq
pi = 2*a
while a!=1:
        
        sq=math.sqrt(2+sq)
        
        a=2/sq
        
        pi*=a
        
print("Approximation of pi:",round(pi,3))

def circle():
        
        rad = eval(input("Enter the radius:\n"))
        area = round(pi * rad**2 , 3)
        print("Area:", area)
        
circle()