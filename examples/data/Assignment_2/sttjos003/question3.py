import math

x=math.sqrt(2)
y=2
while (x<2):
    y=y*(2/x)
    x = math.sqrt(2+x)
    
print("Approximation of pi:",round(y,3))

rad=eval(input("Enter the radius:\n"))

print("Area:", round(y*rad*rad,3))