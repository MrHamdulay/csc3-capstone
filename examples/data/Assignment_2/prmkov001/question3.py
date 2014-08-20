#Kovlin Perumal
#PRMKOV001

from math import *
term = sqrt(2)
pi = 2
while(term!=2) :
   
   pi = pi * 2/ term 
   term = sqrt(2+term)


print("Approximation of pi:",round(pi,3))

rad = eval(input("Enter the radius:\n"))

print("Area:", round(pi*rad**2,3))


  