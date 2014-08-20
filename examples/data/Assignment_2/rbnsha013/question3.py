import math
s = math.sqrt(2)
approx = 1
while 1:
    approx = approx*((2/s))
    s = math.sqrt(2+s)
    if approx==1.5707963267948986:
        break

approx = 2*approx
print("Approximation of pi:", round(approx,3))
print("Enter the radius:")
r = eval(input())
area = round(approx*(r**2),3)
print("Area:", area)