"""program to check if a complete sudoku is valid or not
Kristin Kinmont
9 May 2014"""

# convert input to a 2D array
sudoku = []
numbers = input()
sudoku.append(numbers)
for i in range(8):
    numbers = input()
    sudoku.append(numbers)

error = 0 # counts the number of erros in the grid
    
# check if no 2 cells in a row are the same
col = []
for rows in range(9):
    for cols in range(9):
        if sudoku[rows][cols] not in col:
            col.append(sudoku[rows][cols])
        else:
            error += 1
    col = []

# check if no 2 cells in a column are the same
row = []
for cols in range(9):
    for rows in range(9):
        if sudoku[rows][cols] not in row:
            row.append(sudoku[rows][cols])
        else:
            error += 1
    row = []

# check if no two cells in a block are the same
block = []
for i in [0,3,6]: # check for 1st row of 3x3 blocks
    for row in range(3):
        for col in range(3):
            if sudoku[row][col+i] not in block:
                block.append(sudoku[row][col+i])
            else:
                error += 1
    block = []
    
for i in [0,3,6]: # check for 2nd row of 3x3 blocks
    for row in range(3,6):
        for col in range(3):
            if sudoku[row][col+i] not in block:
                block.append(sudoku[row][col+i])
            else:
                error += 1 
    block = []
    
for i in [0,3,6]: # check for last row of 3x3 blocks
    for row in range(6,9):
        for col in range(3):
            if sudoku[row][col+i] not in block:
                block.append(sudoku[row][col+i])
            else:
                error += 1 
    block = []
    
# check if sudoku valid
if error != 0:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")
