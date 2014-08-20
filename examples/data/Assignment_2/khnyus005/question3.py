import math

pi = 2
den = math.sqrt(2)
c = 1

while c<4:
    pi = pi*2/den
    den = math.sqrt(2+den)
    c+=1
pi3 = round(pi,3)

print("Approximation of pi:",pi3)
r = eval(input("Enter the radius:\n"))

a = round((r**2*pi),3)

print("Area:",a)
