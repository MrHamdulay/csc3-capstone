""" A program to check if a complete Sudoku grid is valid or not
Author: Emiel Zyde
Date: 11 May 2014 """

#We want to get the input from the AM and store it in a 2-D array
sudoku_grid = []   #initialize an empty grid 
for i in range(9):
    x = ",".join(input(""))
    sudoku_grid.append(x)

for i in range(len(sudoku_grid)):
    sudoku_grid[i] = sudoku_grid[i].split(",")
    
#A function to check that no two cells in the same row have the same value   
def check_rows():    
    for row in range(9):
        values = []   #we create an empty list and add values as we encounter them, to check for duplicates
        for col in range(9):
            if sudoku_grid[row][col] in values:
                return False
            else:
                values.append(sudoku_grid[row][col])
    return True

#A function to check that no two cells in the same column have the same value 
def check_cols():
    for col in range(9):
        values = []
        for row in range(9):
            if sudoku_grid[row][col] in values:
                return False
            else:
                values.append(sudoku_grid[row][col])
    return True

#A function to check that no cells in the same 3x3 sub-grid have the same value
def check_subgrid():
    for i in range(0,9,3):
        subgrid = []
        for col in range(i,i+3):
            for row in range(i,i+3):
                subgrid.append(sudoku_grid[row][col])
        subgrid_values = []
        for i in subgrid:
            if i in subgrid_values:
                return False
            else:
                subgrid_values.append(i)
    return True 

#Checks if the various conditions are fulfilled and prints out a statement accordingly 
if check_cols() == True and check_rows() == True and check_subgrid() == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")