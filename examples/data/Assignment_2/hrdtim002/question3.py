import math

def calc_pi():
    x,y = 2,0
    while(y!=2):
        y = math.sqrt(2+y)
        x *= 2/y
    return x

print("Approximation of pi:", round(calc_pi(),3))
r = eval(input("Enter the radius:\n"))
print("Area:", round(calc_pi() * (r*r),3))