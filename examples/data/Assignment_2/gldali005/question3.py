import math
x=math.sqrt(2)
tot=2

while 2/x != 1:
  
  tot=tot*2/x
  x=math.sqrt(2+x)
 
print("Approximation of pi:",round(tot,3))
radius= eval(input("Enter the radius: \n"))
print("Area:", round((radius**2)*tot,3))