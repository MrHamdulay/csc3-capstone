import math
pi = 2;
factor = math.sqrt(2)
count = 1
while(factor!=1 and count<500000):
    pi=pi*(2/factor)
    factor=math.sqrt((2+factor))
    count+=1
print("Approximation of pi:",round(pi,3))
#print(count)
rad = eval(input("Enter the radius:\n"))
print("Area:",round(pi*(rad**2),3))