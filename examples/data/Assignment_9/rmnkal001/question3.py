#Kalind Ramnarayan
#sudoku
#11 May 2014

sudoku = [ ]
correct = True
for i in range(9):
    sudoku.append(input())  # Create list of sudoku lines
grid = [ ]

for i in range(9):                  #split lines into tree parts
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

columns = [[],[],[],[],[],[],[],[],[]]          #create a 2D list 
for i in range(9):                                          
    for j in range(9):
        columns[i].append(sudoku[j][i])
for i in range(9):                              #check if sudoku is correct
    for j in range(9):
        if(grid[i].index(grid[i][j])!=j):
           correct=False

for i in range(9):
    for j in range(9):
        if(sudoku[i].index(sudoku[i][j])!=j):
            correct=False

for i in range(9):
    for j in range(9):
        if(columns[i].index(columns[i][j])!=j):
            correct=False

if(correct):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")