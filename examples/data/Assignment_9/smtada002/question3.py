'''Assignment 9 question 3 Sudoku checker
Adam Smith
12 May 2014'''

grid = []
Complete = True

for i in range (9): #read in the input into the grid
    InputLine = input()
    grid.append([])
    for j in range (9):
        grid[i].append(int(InputLine[j]))
        
columns = set()
for i in range (9): #Checks that all rows and columns have unique values
    if len(set(grid[i])) != 9:
        Complete = False
        break
    for j in range (9):
        columns.add(grid[j][i])
    if len(columns) != 9:
        Complete = False
        break
    columns.clear()
    
block = set()
for startX in range(0,7,3): #Checks the 3x3 blocks within the grid
    for startY in range(0,7,3):
        for i in range (3):
            for j in range (3):
                block.add(grid[i][j])
        if len(block) != 9:
            Complete = False
            break

if Complete:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")