"""program to check if a complete sudoku is valid or not
Muhammad Nabeel Dulymamode
11/05/2014"""

#function to check if sudoku grid is valid
#returns True if valid, otherwise False
def checksudoku(sudoku):
    #Check if rows are valid
    for row in range(0,9):
        for num in range(1,10):
            if not(num in sudoku[row]):
                return False
    #Check if columns are valid
    sudokucols = [0]*9
    for col in range(0,9):
        for row in range(0,9):
            sudokucols[row] = sudoku[row][col]
        for num in range(1,10):
            if not(num in sudokucols):
                return False
    #Check if subgrids are valid
    sudokusubs = [0]*9
    startrow = 0
    startcol = 0
    for sub in range(0,9):
        startrow = (sub // 3) * 3
        startcol = (sub % 3) * 3
        i = 0
        for subrow in range(startrow, startrow+3):
            for subcol in range(startcol, startcol  +3):
                sudokusubs[i] = sudoku[subrow][subcol]
                i += 1
        for num in range(1,10):
            if not(num in sudokusubs):
                return False
    return True #if all conditions are passed

#create sudoku grid
sudoku = []
for row in range(0,9):
    sudoku.append([0]*9)

#input grid in sudoku grid
for i in range(0,9):
    line = input()
    for j in range(0,9):
        sudoku[i][j] = int(line[j])

#check if grid is valid
valid = checksudoku(sudoku)
if valid:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")