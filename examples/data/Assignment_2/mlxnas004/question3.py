import math
x = 0
answer = 0
value = 2
interim_pi = 0

while answer != 1:
 x += 2
 x = math.sqrt(x)
 answer = 2/x
 interim_pi = answer*value
 value = interim_pi
 
 pi = round(interim_pi,3)
  
 
print("Approximation of pi:",pi)
radius = eval(input("Enter the radius:\n"))
area = interim_pi*(radius**2)
area = round(area,3)
print("Area:",area)
 
    
    
    
    
    