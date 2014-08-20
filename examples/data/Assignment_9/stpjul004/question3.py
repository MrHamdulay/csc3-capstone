""" Program to check the validity of a sudoku puzzle
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-05-16 """

def checkDuplicates(list):
    """ Function that checks if a row contains duplicate numbers """
    if len(list) == 1:
        return True
    elif list[0] in list[1:]:
        return False
    else:
        return checkDuplicates(list[1:])

# Get a sudoku puzzle
inputPuzzle = []

i = 0
while i < 9:
    i += 1
    inputPuzzle.append(input())
    
# Create a 2D 9x9 array
sudokuPuzzle = []

for i in range(9):
    sudokuPuzzle.append([0]*9)

# Put the data into the 9x9 grid
for row in range(len(inputPuzzle)):
    for i in range(len(inputPuzzle[row])):
        sudokuPuzzle[row][i] = eval(inputPuzzle[row][i])

valid = True

# Check rows
for row in range(len(sudokuPuzzle)):
    if not checkDuplicates(sudokuPuzzle[row]):
        valid = False

# Check columns
for col in range(len(sudokuPuzzle[0])):
    column = []
    # Extract a single column
    for i in range(len(sudokuPuzzle)):
        column.append(sudokuPuzzle[i][col])
    # Check for duplicates in the column
    if not checkDuplicates(column):
        valid = False
        

# Check 3x3 subgrids
# Iterate throught the "start" points of each sub grid i.e. row 0,3,6; col 0,3,6
# "i" is the start point co-ord for the row of the subgrid
# "j" is the start point co-ord for the column of the subgrid
for i in range(0,9,3):
    for j in range(0,9,3):
        subgrid = []
        # Extract a subgrid as a single array to check for duplicates
        # Iterate through each item in the subgrid
        for sub_y in range(i,i+3):
            for sub_x in range(j,j+3):
                subgrid.append(sudokuPuzzle[sub_y][sub_x])
        if not checkDuplicates(subgrid):
            valid = False

if valid:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")