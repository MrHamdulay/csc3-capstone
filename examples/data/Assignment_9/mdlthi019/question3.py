"""Program to check if a complete Sudoku grid is valid or not
Thiloshni Moodley
14 May 2014"""

sudoko = [] #create empty list
case = True
for i in range(9):
    sudoko.append(input())
grid = [] #create empty list

#appending to sudoko list with slicing
for i in range(9):
    grid.append(sudoko[i][0:3])
for i in range(9):
    grid.append(sudoko[i][3:6])
for i in range(9):
    grid.append(sudoko[i][6:9])
i=0

while(i<len(grid)): #execute if i is less than the length of the grid
    grid[i]=grid[i]+grid[i+1]+grid[i+2]
    grid.remove(grid[i+1])
    grid.remove(grid[i+1])
    i=i+1 #changes value of i 

#conditons
columns = [[],[],[],[],[],[],[],[],[]] # 9 columns
for i in range(9):
    for j in range(9):
        columns[i].append(sudoko[j][i]) #appends 
for i in range(9):
    for j in range(9):
        if(grid[i].index(grid[i][j])!=j):
           case=False
for i in range(9):
    for j in range(9):
        if(columns[i].index(columns[i][j])!=j):
            case=False
for i in range(9):
    for j in range(9):
        if(sudoko[i].index(sudoko[i][j])!=j):
            case=False
            
if(case): #If the case is true, the grid is valid
    print("Sudoku grid is valid")
else: # The grid is invalid
    print("Sudoku grid is not valid")