#NDXMIC014
#ASSIGNMENT 9
#QUESTION 2

sudoku_1 = [ ]

flag = True

for i in range(9):
    sudoku_1.append(input())
grid_1 = [ ]

for i in range(9):
    grid_1.append(sudoku_1[i][0:3])

for i in range(9):
    grid_1.append(sudoku_1[i][3:6])

for i in range(9):
    grid_1.append(sudoku_1[i][6:9])
i=0

while(i<len(grid_1)):
    grid_1[i]=grid_1[i]+grid_1[i+1]+grid_1[i+2]
    grid_1.remove(grid_1[i+1])
    grid_1.remove(grid_1[i+1])
    i=i+1

col = [[],[],[],[],[],[],[],[],[]]

for i in range(9):
    for j in range(9):
        col[i].append(sudoku_1[j][i])

for i in range(9):
   
    for j in range(9):
        if(grid_1[i].index(grid_1[i][j])!=j):
           flag=False
for i in range(9):
    for j in range(9):
        if(col[i].index(col[i][j])!=j):
            flag=False

for i in range(9):
    for j in range(9):
        if(sudoku_1[i].index(sudoku_1[i][j])!=j):
            flag=False

if(flag):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")