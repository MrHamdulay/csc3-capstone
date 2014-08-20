import math
j=math.sqrt(2)
a=2/j
products=2*a
while a!=1:
        
        j=math.sqrt(2+j)
        a=2/j
        products*=a
        
print("Approximation of pi:",round(products,3))

def area():
        r=eval(input("Enter the radius:\n"))
        a=round(products*r**2,3)
        print("Area:",a)
        
area()