

import math

equation = input("Enter a function f(x):\n")
equation = equation.lower()
#print("The equation is:", equation)

grid = []
for a in range (10):
    grid.append([" "]*21)
    
for b in range (1):
    grid.append(["-"]*21)
    
for c in range (11):
    grid.append([" "]*21)

for d in range(21):
    grid[d][10] = "|"

grid[10][10]="+"
  
    

    

for x in range(-10,11):
    y = eval(equation)
    y = round(y)
    #print(x,y)
    
    if y <= 10:
        px = x +10
        py = 20-(y + 10)
        #print(px,py)
        grid[py][px] = "o"
    
for row in range(21):
    for col in range(21):
        print ( grid[row][col], end = "")
                
    print()
          