import math
x = math.sqrt(2)
total = 2
while 2/x != 1:  
   total = total * 2/x
   x = math.sqrt(2 + x) 
print ("Approximation of pi:",round(total,3))
radius = eval (input ("Enter the radius:\n"))
print("Area:",round((radius**2)*total,3))

