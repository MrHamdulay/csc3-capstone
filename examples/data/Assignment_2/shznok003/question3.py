import math
n= math.sqrt(2)
pi=2* (2/n)
while (n!=2):
    n= math.sqrt(2+n)
    pi = pi* (2/n) 
print ("Approximation of pi:" ,round(pi,3))
rad=0
rad = eval(input("Enter the radius: \n"))
print ("Area:" ,round(pi*rad**2,3))