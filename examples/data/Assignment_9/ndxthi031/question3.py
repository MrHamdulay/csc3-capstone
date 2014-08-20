grid = [ ]
boole = True
for i in range(9):
    grid.append(input())
arr = [ ]

for i in range(9):
    arr.append(grid[i][0:3])
for i in range(9):
    arr.append(grid[i][3:6])
for i in range(9):
    arr.append(grid[i][6:9])
i=0
while(i<len(arr)):
    arr[i]=arr[i]+arr[i+1]+arr[i+2]
    arr.remove(arr[i+1])
    arr.remove(arr[i+1])
    i=i+1

col = [[],[],[],[],[],[],[],[],[]]
for i in range(9):
    for j in range(9):
        col[i].append(grid[j][i])
for i in range(9):
    for j in range(9):
        if(arr[i].index(arr[i][j])!=j):
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