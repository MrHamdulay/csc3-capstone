# Assignment 9 - question3.py
# BXTNAA002
# May 2014

grid = []     #create a 2D array
lines = [] 

for i in range(0, 9):            
    line = input("")
    for i in line:
        lines.append(i) #add numbers to the 1st array
    grid.append(lines) #add 1st array to grid
    lines = [] #initialize the 1st array as empty to collect a new set of numbers

def check_sum_row(grid): # check if the sum of each row in the sudoku grid equals 45 as the sum of numbers from 1 to 9 is equal to 45
    for i in range(0, 9):
        the_rsum = 0
        y = 0
        for j in range(0, 9):
            the_rsum += int(grid[j][i])
        if the_rsum != 45: 
            y=1
        else:
            continue
        if y == 1:
            return False #return False if the sum is not equal to 45
        else:
            continue    

def check_sum_col(grid): #check if the sum of each column in the sudoku grid equals 45 as the sum of numbers from 1 to 9 is equal to 45
    for i in range(0,9):
        the_csum = 0
        z = 0
        for j in range(0,9):
            the_csum += int(grid[i][j])
        if the_csum != 45:
            z=1
        else:
            continue
        if z == 1:
            return False #return false if the sum is not equal to 45
        else:
            continue

def check_3x3_grid(sudoku): #check if sum of a 3x3 grid within the sudoku grid is equal to 45
    thesum = 0
    for i in range(0, 3):
        for j in range(0, 3):
            thesum += int(grid[i][j])
    if thesum != 45:
        return False
    
if check_sum_col(grid) == False or check_sum_row(grid) == False or check_3x3_grid(grid) == False:
    print("Sudoku grid is not valid") # the sudoku grid is not valid if both functions return False
else:
    print("Sudoku grid is valid")