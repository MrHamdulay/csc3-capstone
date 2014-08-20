#Yaseen Sayed Ismail
#SYDYAS003
#11/05/2014
#Program to check the validity of a grid as a sudoku

sudoku = [ ]#Define grid
flag = True#Initialise flag for later use

#Loop to allow user to input grid
for i in range(9):
    sudoku.append(input())
    
grid = [ ]#Defined list grid to store each 3x3 grid

#Populate list grid
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

columns = [[],[],[],[],[],[],[],[],[]]#Define list columns to store each column
for i in range(9):
    for j in range(9):
        columns[i].append(sudoku[j][i])

#Checks if there are any duplicates in 3x3 grids
for i in range(9):
    for j in range(9):
        if(grid[i].index(grid[i][j])!=j):
           flag=False
           
#Checks if there are any duplicates in columns
for i in range(9):
    for j in range(9):
        if(columns[i].index(columns[i][j])!=j):
            flag=False
            
#Checks if there are any duplicates in rows
for i in range(9):
    for j in range(9):
        if(sudoku[i].index(sudoku[i][j])!=j):
            flag=False

#Prints valid if flag is true and invalid if flag is false
if(flag):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")