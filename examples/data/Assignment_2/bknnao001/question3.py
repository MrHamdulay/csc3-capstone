import math
pi= 2
x= math.sqrt(2)
y= 2/x

while y!= 1 :      
    pi = pi*y
    x = math.sqrt(2 + x)
    y = 2/x

print("Approximation of pi:", end=" ")
print(round(pi*y,3))

radius = eval(input("Enter the radius: \n"))
print("Area:",round(pi*y*radius*radius,3)) 


