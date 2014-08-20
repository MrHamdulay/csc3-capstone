# program to write calulate area


import math
pi= 2
b= math.sqrt(2)
a= 2/b

while a!= 1 :      # I must approximate pi
    pi = pi*a
    b = math.sqrt(2 + b)
    a = 2/b

print("Approximation of pi:", end=" ")
print(round(pi*a,3))

radius = eval(input("Enter the radius: \n"))
print("Area:",round(pi*a*radius*radius,3))   # use radius of circle formulae


