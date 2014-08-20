import math
def f(n):
      if (n == 1):
            return math.sqrt(2)
      else:
            return math.sqrt(2 + f(n-1))
pi=2
x=1
while (f(x)!=2):
      pi=pi*(2/f(x))
      x=x+1
print("Approximation of pi:", round(pi,3))
radius=eval(input("Enter the radius:\n"))
area=pi*radius**2
print("Area:", round(area,3))
