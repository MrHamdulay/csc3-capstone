"""Pogram to check if sodoku is valid
Micaela Narasmulu
17 May 2014"""

grid = [ ]
boole = True
for i in range(9):
    grid.append(input())
array = [ ]

for i in range(9):
    array.append(grid[i][0:3])
for i in range(9):
    array.append(grid[i][3:6])
for i in range(9):
    array.append(grid[i][6:9])
i=0
while(i<len(array)):
    array[i]=array[i]+array[i+1]+array[i+2]
    array.remove(array[i+1])
    array.remove(array[i+1])
    i=i+1

col = [[],[],[],[],[],[],[],[],[]]
for i in range(9):
    for j in range(9):
        col[i].append(grid[j][i])
for i in range(9):
    for j in range(9):
        if(array[i].index(array[i][j])!=j):
           boole=False
for i in range(9):
    for j in range(9):
        if(col[i].index(col[i][j])!=j):
            boole=False
for i in range(9):
    for j in range(9):
        if(grid[i].index(grid[i][j])!=j):
            boole=False
if(boole):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")