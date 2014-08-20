import math
x = 4
y = math.sqrt(2)
z= math.sqrt(2)
while z<2:
    x = x*2
    z = (math.sqrt(2+z))
    y = y*z
ans = x/y
ans = round(ans,3)
print("Approximation of pi:", ans)
x = eval(input("Enter the radius:\n"))**2
print("Area:", round(x*(math.pi), 3))