import math
x=math.sqrt(2)
pie=2
while True:
    pie=pie*(2/x)
    x=math.sqrt(2+x)
    
    if x==2:
        break
    

finalpi= round(pie,3)


print("Approximation of pi:",finalpi)


radius=eval(input("Enter the radius:""\n"))
area=pie*radius*radius
finalarea=round(area,3)
print("Area:", finalarea)