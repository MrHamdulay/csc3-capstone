#EDLADA002                                     
import math     



pi = 1
divisor = 0
term =2

while(term != 1):
  pi*=term
  term = 2/math.sqrt(2+divisor)
  divisor= math.sqrt(2+divisor)

print("Approximation of pi:",round(pi,3))
rad = eval(input("Enter the radius:\n"))


print ("Area:",(round(rad*rad*pi,3)))