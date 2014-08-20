# Program checks if suddoku grid is valid
# Wandile Lesejane
# 16 May 2014

import math

grid=[]
lis=[]
for i in range(9):
    line=input()
    for j in range(9):
        lis.append(eval(line[j]))
    grid.append(lis)
    lis=[]
    
def horizontal_check(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            y=grid[i].count(j)
           
        if y>1:
            return False
        else:
            return True

def vertical_check(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            y=grid[j].count(i)
            
        if y>1:
            return False
        else:
            return True

if vertical_check(grid)==False or horizontal_check(grid)==False:
    print('Sudoku grid is not valid')
else:
    print('Sudoku grid is valid')
    