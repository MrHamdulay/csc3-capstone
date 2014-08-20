import math

print 
i = 2
j= math.sqrt(2)
val = 0
pi = 1
count = 0

while count<100:    
 val = i/j
 j = math.sqrt(2 + j)
 pi = pi * val
 count = count + 1

pi = pi*2
print("Approximation of pi:", round(pi,3))

radius = eval(input("Enter the radius:\n"))

print ("Area:", round(pi*(radius*radius),3))
