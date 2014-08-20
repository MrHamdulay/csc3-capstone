"""CHTGEN002
12/05/14
Sudoku
"""
sudoku = []
flag = True
grid = []
max=9
i=0

for h in range(max):
    sudoku.append(input())

for j in range(max):
    grid.append(sudoku[j][0:3])

for k in range(max):
    grid.append(sudoku[k][3:6])

for l in range(max):
    grid.append(sudoku[l][6:9])

while(len(grid)>i):
    grid[i]=grid[i]+grid[i+1]+grid[i+2]
    grid.remove(grid[i+1])
    grid.remove(grid[i+1])
    i+=1

columns = [[],[],[],[],[],[],[],[],[]]
for k in range(max):
    for j in range(max):
        columns[k].append(sudoku[j][k])

for k in range(max):
    for j in range(max):
        if(grid[k].index(grid[k][j])!=j):
            flag=False

for k in range(max):
    for j in range(max):
        if(columns[k].index(columns[k][j])!=j):
            flag=False

for k in range(max):
    for j in range(max):
        if(sudoku[k].index(sudoku[k][j])!=j):
            flag=False
if(flag):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")