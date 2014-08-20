# Assignment 3 Question 2
# Isosceles triangle
height=eval(input("Enter the height of the triangle:"))

for i in range(0,height+1,1):
       print((height-i)*" ","*"*(2*i-1),sep="")
      