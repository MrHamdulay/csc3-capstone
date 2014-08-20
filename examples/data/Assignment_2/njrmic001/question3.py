#question3.py
#A program to calculate the value of PI, compute and display the area of a circle with radius entered by the user
#Author: Michelle Njoroge

from math import*

a=2
b=sqrt(2)
pi=2*(a/b)
while b<2:
    b=sqrt(2+b)
    pi=pi*(a/b)

print("Approximation of pi:",round(pi,3))
y=eval(input("Enter the radius:\n"))
Area=round((pi*y**2),3)
print("Area:",round((pi*y**2),3))

      

      
     


    
    
    
          