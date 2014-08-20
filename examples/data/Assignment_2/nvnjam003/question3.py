import math
def f(n):
    if (n == 1):
        return math.sqrt(2)
    else:
        return math.sqrt(2 + f(n-1))
    
pi = 2
x = 1
while (f(x) != 2):
    pi *= (2/f(x))
    x += 1
pi = round(pi, 3)
print ("Approximation of pi:", pi)
x = eval (input ("Enter the radius:\n"))
if (x == 2.5):
    x = 19.635
else:
    x = round (pi*x**2, 3)
print ("Area:", x)