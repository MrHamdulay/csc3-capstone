# Student number: FRDYON001
# Name: Yonela Ford
# Programme to give area of a circle
# 9 March 2014

import math
b=0
ans=2*2/(math.sqrt(2))
a=math.sqrt(2)
c=0

while c!=1:
  
    b=math.sqrt(2+a)
    
    c=2/b
    ans=ans*(c)
    a=b
print("Approximation of pi:",round(ans,3)) 
x=eval(input("Enter the radius:\n"))
print("Area:",round((ans*x**2),3))

