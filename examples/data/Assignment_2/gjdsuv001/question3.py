import math
pi = 2

d = 0
n = math.sqrt(2)
x = 2/n

while d != 1:
    n = math.sqrt(2+n)
    d = 2/n
    x = x*d
    
pi = pi *x
print("Approximation of pi:",round(pi,3))


b = eval(input("Enter the radius:\n"))
print("Area:", round((b**2)*pi,3))


