import math
num=2
dem=math.sqrt(2)
term = num/dem
ans=2
ans=ans*(num/dem)
while term>1:
    dem=math.sqrt(2+dem)
    term=num/dem
    ans=ans*(num/dem)
print("Approximation of pi:", round(ans,3))
x=eval(input("Enter the radius:\n"))
area=ans*x*x
print("Area:", round(area,3))