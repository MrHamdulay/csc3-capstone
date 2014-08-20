# Program to graph functions by using a grid
# hendrik Joosten
# 17 april 2014


# importing the math module in python to handle certain functions
import math
# asking the user for input
user_function = input("Enter a function f(x):\n")



# this is a for loop to draw the graph line by line block by block
# it will form a grid 21 blocks wide and 21 block high

# a for loop representing the lines (rows)
for y in range(10,-11,-1):
      # a for loop representing the columns
      for x in range(-10,11):
            # this if represent point on the function
            # rounded to have a greater hit rate
            if y == round((eval(user_function))):
                  print("o",end="")
            # this exeption prints the origin (+)
            elif x == 0 and y == 0:
                  print("+",end="")
            # this is the printing of the x axis
            elif y == 0:
                  print("-",end="")
            # this is the printing of the y axis
            elif x == 0:
                  print("|",end="")
            # this prints the empty bock on the graph
            else:
                  print(" ",end="")
                  
      # this goes to the next row in the graph
      print("")
            



