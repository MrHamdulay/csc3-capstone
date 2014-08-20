#program to check if a complete Sudoku grid is valid or 
#KNNSAD001
#Assignment 9

sudoku_ = [ ]
condition = True
for i in range(9):
    sudoku_.append(input())
grid_ = [ ]

for i in range(9):
    grid_.append(sudoku_[i][0:3])
for i in range(9):
    grid_.append(sudoku_[i][3:6])
for i in range(9):
    grid_.append(sudoku_[i][6:9])
i=0

while(i<len(grid_)):
    grid_[i]=grid_[i]+grid_[i+1]+grid_[i+2]
    grid_.remove(grid_[i+1])
    grid_.remove(grid_[i+1])
    i=i+1

columns_ = [[],[],[],[],[],[],[],[],[]]
for i in range(9):
    for j in range(9):
        columns_[i].append(sudoku_[j][i])
for i in range(9):
    for j in range(9):
        if(grid_[i].index(grid_[i][j])!=j):
            condition=False
for i in range(9):
    for j in range(9):
        if(columns_[i].index(columns_[i][j])!=j):
            condition=False
for i in range(9):
    for j in range(9):
        if(sudoku_[i].index(sudoku_[i][j])!=j):
            condition=False
            
if(condition):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")