import math # makes the maths library available.
a=2 #the first number in the terms
n=math.sqrt(2) #the second number in the terms
pi=a*(a/n)
while n!=2:
    n= math.sqrt(a + n)
    pi=pi * a/n
print("Approximation of pi:" ,round(pi,3))
r=eval(input("Enter the radius:\n"))
Area=pi * r**2
print("Area:" ,round(Area,3))
       