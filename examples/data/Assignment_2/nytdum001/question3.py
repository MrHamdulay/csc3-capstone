#Dumisani J Nyathi
#Copmuting with numbers:)
#13 March 2014
import math
def area():
    x=math.sqrt(2)
    a=2*(2/x)
    b=(2/math.sqrt(2+x))
    c=(2/math.sqrt(2+(math.sqrt(2+x))))
    d=(2/math.sqrt(2+(math.sqrt(2+(math.sqrt(2+x))))))
    e=(2/math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+x))))))))
    f=(2/math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+x))))))))))
    g=(2/math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+x))))))))))))
    h=(2/math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+x))))))))))))))
    i=(2/math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+(math.sqrt(2+x))))))))))))))))
    pi=a*b*c*d*e*f*g*h*i
    print("Approximation of pi:",round(pi,3))
    y=eval(input("Enter the radius:\n"))
    print("Area:",round((pi*y**2),3))
    
area()