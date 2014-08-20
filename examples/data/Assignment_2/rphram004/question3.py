import math
a = math.sqrt(2)
pi = 2*(2/a)
while (a!=2):
    a = math.sqrt(2+a)
    pi = pi*(2/a)
b = round(pi,3)
print("Approximation of pi:", b)
x = eval(input("Enter the radius:\n"))
y = (pi*x**2)
z = round(y,3)
print("Area:" ,z)