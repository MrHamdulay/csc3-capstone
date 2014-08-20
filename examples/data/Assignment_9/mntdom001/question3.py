""" a program to check if a complete Sudoku grid is valid or not.
Dominic Manthoko
11 May 2014
"""

from copy import *
    
def check_row(Sudoku):
    ''' a function that will check if there are any matching numbers in a row
    Returns True if there are no matching values and False if there are'''
    
    for item in Sudoku:
        s = []
        for val in item:
            if val not in s:            
                s.append(val)       # adds the value only if it not already in the list s
            elif val in s:
                return False        #  a value is already in the list then there is a repetition of some value  
    return True


def check_column(Sudoku):
    ''' a function that will check the columns of the grid and determine whether or
    not there are matching items/values'''
    
    Sudoku_copy = deepcopy(Sudoku)
    sym(Sudoku_copy)
    if check_row(Sudoku_copy):
        return True
    return False
    
def sym(grid):
    """ a function that switches the values in a grid"""
    grid_copy = deepcopy(grid)
    for y in range(9):
        for x in range(9):
            grid[x][y]=grid_copy[y][x]
            
def check_3x3(Sudoku):
    ''' a function to check the 3x3 grids within a 9x9'''
    
    grid_copy = deepcopy(Sudoku)
    box = []
    
    for y in range(0,7,3):
        for x in range(0,7,3):
            s = ''
            s += grid_copy[y][x] + grid_copy[y][x+1] + grid_copy[y][x+2] + grid_copy[y+1][x] + grid_copy[y+1][x+1] + grid_copy[y+1][x+2] + grid_copy[y+2][x] + grid_copy[y+2][x+1] + grid_copy[y+2][x+2]
            box.append(s)
            
    # check that each string  in the box list contains unique values
    for string in box:
        check_item = []
        for char in string:
            if char not in check_item:
                check_item.append(char)
            elif char in  check_item:
                return False
    return True
            
            
def check_small_grid_vert(Sudoku):
    """ function that will check the vertical values with a grid"""
    
    grid_copy == deepcopy(Sudoku)
    sym(grid_copy)
    if check_small_grid(grid_copy):     # if the check_grid_grid function returns true, then this function must also return True
        return True
    return False

if __name__ == '__main__':
    # creat an empty array
    Sudoku = []
    
    for line in range(9):
        # prompt the user to input a list of digits
        l = input()
        
        l = list(l)
        Sudoku.append(l)    
        
    if check_row(Sudoku) and check_column(Sudoku) and check_3x3(Sudoku):
        print('Sudoku grid is valid')
    else:
        print('Sudoku grid is not valid')
  