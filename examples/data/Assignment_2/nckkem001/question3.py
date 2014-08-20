import math
g=0
i=2
while (g)!=1:
        g=math.sqrt(2+g)
        i=i*(2/g)
        if (2/g)==1: break
print("Approximation of pi:", round(i,3))
x=eval(input("Enter the radius: \n"))
y=i*x*x
print("Area:", round(y,3))