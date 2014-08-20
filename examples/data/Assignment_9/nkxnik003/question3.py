sudoku = [ ]
flag = True
for i in range(9):
#Nikhil Jiten Naik
#NKXNIK003
#Assignement 9-Question 3

    sudoku.append(input())
grid = [ ]

for i in range(9):
    grid.append(sudoku[i][0:3])
for i in range(9):
    grid.append(sudoku[i][3:6])
for i in range(9):
    grid.append(sudoku[i][6:9])
i=0
while(i<len(grid)):
    grid[i]=grid[i]+grid[i+1]+grid[i+2]
    grid.remove(grid[i+1])
    grid.remove(grid[i+1])
    i=i+1

columns = [[],[],[],[],[],[],[],[],[]]
for i in range(9):
    for j in range(9):
        columns[i].append(sudoku[j][i])
for i in range(9):
    for j in range(9):
        if(grid[i].index(grid[i][j])!=j):
            flag=False
for i in range(9):
    for j in range(9):
        if(columns[i].index(columns[i][j])!=j):
            flag=False
for i in range(9):
    for j in range(9):
        if(sudoku[i].index(sudoku[i][j])!=j):
            flag=False
if(flag):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")