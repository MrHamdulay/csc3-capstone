#approximation of pi
import math

y=0
pi = 2
demon = 0
while(pi != y):
    y = pi
    demon = math.sqrt(2 + demon)
    pi = pi*(2/demon)
    
pi = round(pi,3)

"""Approximation of pi: 3.142
Enter the radius:
2.5
Area: 19.635"""

print("Approximation of pi:",pi)
r = eval(input("Enter the radius:\n"))
area = math.pi*(r**2)
print("Area:", round(area,3))
  
        