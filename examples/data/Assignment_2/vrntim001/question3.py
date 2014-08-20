import math
y = 0
count = 0
x = 2
for i in range(100000):
    count = count + 1
    numerator = 2
    denominator = math.sqrt(2 + (y))
    y = denominator
    m = numerator/denominator
    x = x * m

print("Approximation of pi:",round(x,3 ))
r = eval(input("Enter the radius:\n"))
a = x*r**2
print("Area:",round(a,3))