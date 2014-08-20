import math
#intialize variables
pi=2 
countsq=math.sqrt(2)
term=2/countsq
pi=pi*(term)

while term!=1:
 countsq=math.sqrt(2+countsq)
 term= 2/countsq
 pi=pi*term
  
print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
area=pi*radius**2
print("Area:",round(area,3))


 

