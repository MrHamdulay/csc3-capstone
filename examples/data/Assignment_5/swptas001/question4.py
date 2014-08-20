'''A program for drawing user defined graphs in a 20 by 20 grid'''
### Tashiv Sewpersad
### Assignment 5 - Question 4
### 14 - 04 - 2014

## Uses
import math

## Live Code
# Generate Blank Grid
BaseGraph = []
for y in range(-10,11,1):
  Yline = []
  for x in range(-10,11,1):
    if (x == 0) and (y != 0):
      Yline.append("|")
    elif (y == 0) and (x == 0):
      Yline.append("+")
    elif (y==0) and (x != 0):
      Yline.append("-")
    else:
      Yline.append(" ")
  BaseGraph.append(Yline)

# Get User defined graph
sFunction = input("Enter a function f(x):\n")

# Print the graph
for y in range(10,-11,-1):
  for x in range(-10,11):
    xPoint = round(eval(sFunction)) # Evalutes with x as a value
    if xPoint == y: # Checks for a graph point
      print("o",end="")
    else:
      print(str(BaseGraph[y+10][x+10]),end="") # Prints when graph point not found
  print("")
