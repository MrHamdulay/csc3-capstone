import math

ans = 2
ans2 = math.sqrt(2)

while 2/ans2 != 1:
       ans = ans*(2/ans2)
       ans2 = math.sqrt(2 + ans2)   

print("Approximation of pi:",round(ans,3))
radius = eval(input("Enter the radius:""\n"))
Area = round(ans*radius**2,3)
print("Area:",Area)

