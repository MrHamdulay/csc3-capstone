#Assignment 2: Question 3
#Asil Motala
#MTLASI002
import math
q=math.sqrt(2)
p=2
while 2/q!=1:
    s=2/q
    p*=s
    q=math.sqrt(2+q)
print("Approximation of pi:",round(p,3))
y=eval(input("Enter the radius:\n"))
print("Area:",round(p*y*y,3))