""" a program to check if a complete sudoku grid is valid or not
joshua wort
16 May 2014"""

#create empty sudoku grid
sudoku_grid=[]
for i in range(9):
    input_lines=input() #user must input each line
    sudoku_grid.append(input_lines) #append each line to the sudoku grid

#function to check if no 2 cells in the same row have the same value    
def check_rows():
    for i in range(len(sudoku_grid)):
        for row in range(9):
            for col in range(1,10):
                test_rows=str(sudoku_grid)[i].count(str(col))
                if test_rows>1:
                    return False
    return True

#function to check if no 2 cells in the same column have the same value    
def check_columns():
    for i in range(len(sudoku_grid)):
        for col in range(9):
            for row in range(1,10):
                test_columns=str(sudoku_grid)[i].count(str(row))
                if test_columns>1:
                    return False
    return True

#function to check if no 2 cells in the same 3x3 subgrid have the same value
def check_subgrid():
    for i in range(0,9,3):
        sub_grid=[]
        for col in range(i,i+3):
            for row in range(i,i+3):
                sub_grid.append(sudoku_grid[row][col])
        subgrid_values=[]
        for i in sub_grid:
            if i in subgrid_values:
                return False
            else:
                subgrid_values.append(i)
    return True

#check if all conditions are met and if so the sudoku grid is valid
if check_rows()==True and check_columns()==True and check_subgrid()==True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
    
                