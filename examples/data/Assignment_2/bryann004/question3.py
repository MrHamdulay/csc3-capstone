import math


den=math.sqrt(2)
totalnum=4
totalden=math.sqrt(2)

while den<2:   
    den=math.sqrt(2+den)
    totalden=totalden*den
    totalnum=totalnum*2
    pi=totalnum/totalden
    
roundpi=round(pi,3)
print("Approximation of pi:", roundpi)

r=float(input("Enter the radius:\n"))
A=round(pi*r*r,3)

print("Area:",A)