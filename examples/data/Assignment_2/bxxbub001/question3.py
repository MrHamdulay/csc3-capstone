import math

x = math.sqrt(2)
num = 1
pi =2
t=0

while t != 1:
    t =2/x
    x = math.sqrt(2 + x)
    pi= pi*t
    #print(pi)
    
print("Approximation of pi:",round(pi,3))
rad = eval(input("Enter the radius:\n"))
area = round(pi*(rad**2),3)
print("Area:",area)

          
    