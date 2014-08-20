import math
den = math.sqrt(2)
pi = 2*2/den
while den != 2:
    den = math.sqrt(2+den)
    pi=pi*2/den
print ("Approximation of pi:",round(pi,3))
rad = eval(input("Enter the radius:\n"))
print("Area:",round(pi*rad**2,3))
      
