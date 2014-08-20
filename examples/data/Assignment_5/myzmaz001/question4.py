""""
Mazwi Myeza
16 April 2014
Assignment5
Question4
"""

import math
#getting funxtion from user
function = input("Enter a function f(x):\n")
#setting up arrays
x1 = []
grid = []
y = []
#calculating y and x values, storint them in arrays#
""""for j in range(21):
    x = j - 10
    f = eval(function)
    y.append((round(f)))
    x1.append((x))
    """
#Making a block
for i in range(21):
    grid.append([0]*21)
#Modifying block to be catesian plane    
for row in range(21):
    
    for col in range(21):
        x = col - 10
        f = eval(function)
        y = round(f)
        if row == 10 - y and col == 10 + x:
            grid[row][col] = "o"
            print(grid[row][col], end = "")        
        elif row == 10 and col == 10:
            grid[row][col]= "+"
            print(grid[row][col], end = "")
        elif col == 10:
            grid[row][col] = "|"
            print(grid[row][col], end = "")
        elif row == 10:
            grid[row][col] ="-"
            print(grid[row][col], end = "")
        else:
            grid[row][col] = " "
            print(grid[row][col], end = "")
    print()        
#ploting function on cartesian plane and printing it       
""""for row in range(21):
    for col in range(21):
        if row == 10 - y[row] and col == 10 + x1[col]:
            grid[row][col] = "o"
            print(grid[row][col], end = "")
        else:
            print(grid[row][col], end = "")
        
    print() 
    """
        