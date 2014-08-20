"""a program to check if a sudoku grid is a valid grid
by Jeremy Smith SMTJER002
15 May 2014"""

def check_row(sudoku):
    """checks if there are any duplicated numbers in a row"""
    for row in range(len(sudoku)):
        for col in range(len(sudoku)):
            if sudoku[row].count(sudoku[row][col]) != 1:
                return True #returns True is there is more than two of the same numbers in a row
            

def check_col(sudoku):
    """checks if there are any duplicated numbers in a column"""
    for col in range(9):
        for row in range(8):
            test = sudoku[row][col]
            for i in range(row+1,9):
                if sudoku[i][col] == test:
                    return True #returns True is there is more than two of the same numbers in a column
         
#captures the sudoku grid as a string as the grid is received as an input
sudoku_str=''
for i in range(9):
    sudoku=input()
    sudoku_str += sudoku

#converts the string of the sudoku grid input into a 2x2 grid
sudoku = []
for row in range(9):
    sudoku_list = []
    for col in range(9):
        sudoku_list.append(sudoku_str[(row*9)+col])
    sudoku.append(sudoku_list)

#converts the 2x2 grid listed by row, to a 2x2 grid listed by each 3x3 sub grid
sudoku_sqr=[]
counter2 = 0
for i in range(3):
    counter1 = 0
    for j in range(3):
        sudoku_list=[]
        for row in range(3):
            for col in range(3):
                sudoku_list.append(sudoku[row+counter2][col+counter1])
        counter1 += 3
        sudoku_sqr.append(sudoku_list)
    counter2 += 3

same_row = check_row(sudoku) #runs the row check function on the inputted sudoku grid
same_column = check_col(sudoku) #runs the column check function on the inputted sudoku grid
same_grid = check_row(sudoku_sqr) #uses the row check function to check that the same is true for the 3x3 sub grids

if same_row == True or same_column == True or same_grid == True:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")