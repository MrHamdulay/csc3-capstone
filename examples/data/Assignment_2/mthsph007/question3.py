#Sphiwe Muthwmbi
#Question 3

#PI
def making_PI():
    import math

    r= 1/math.sqrt(2)
    i= 2
    while i > 1:
        d= i*r
    else:
        d= round(i,3)
        print("Approximation of pi:",d)
  
def call_pi():
    import math
    p= round(math.pi,3)
    print("Approximation of pi:",p)


call_pi()
radius= eval( input("Enter the radius:\n"))
import math
area= round(math.pi*(radius**2),3) 

print("Area:",area)
