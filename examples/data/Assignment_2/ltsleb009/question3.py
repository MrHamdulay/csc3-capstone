import math
x = math.sqrt(2)
ans = 2
while 2/x > 1:
    ans = ans*2/x
    x = math.sqrt(2+x)
print("Approximation of pi:", round(ans,3))
radius = eval(input("Enter the radius:\n"))
area = round((radius**2)*ans, 3)
print("Area: {0}" .format(area))