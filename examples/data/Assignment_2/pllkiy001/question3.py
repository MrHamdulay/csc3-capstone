import math
numerator=2 
denominator=0 
pi=2
count=1 
while(denominator<2):
    denominator=math.sqrt(denominator+2)
    term=numerator/denominator
    pi*=term
    count+=1
print ("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius:\n"))
a=pi*(r**2)
print ("Area:",round(a,3))
    