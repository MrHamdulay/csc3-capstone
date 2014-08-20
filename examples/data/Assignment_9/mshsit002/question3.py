""" a program to check if a complete Sudoku grid is valid or not.
sithembiso Mashinini
19 May 2014
"""

from copy import *
def check1(Sudoku):

    
    for item in Sudoku:
        s = []
        for val in item:
            if val not in s:            
                s.append(val)      
            elif val in s:
                return False          
    return True


def check_column(Sudoku):
   
    
    Sudoku_copy = deepcopy(Sudoku)
    sym(Sudoku_copy)
    if check1(Sudoku_copy):
        return True
    return False
    
def sym(grid):
   
    grid_copy = deepcopy(grid)
    for y in range(9):
        for x in range(9):
            grid[x][y]=grid_copy[y][x]
            
def check_3x3(Sudoku):
   
    
    grid_copy = deepcopy(Sudoku)
    box = []
    
    for y in range(0,7,3):
        for x in range(0,7,3):
            s = ''
            s += grid_copy[y][x] + grid_copy[y][x+1] + grid_copy[y][x+2] + grid_copy[y+1][x] + grid_copy[y+1][x+1] + grid_copy[y+1][x+2] + grid_copy[y+2][x] + grid_copy[y+2][x+1] + grid_copy[y+2][x+2]
            box.append(s)
            
   
    for string in box:
        check_item = []
        for char in string:
            if char not in check_item:
                check_item.append(char)
            elif char in  check_item:
                return False
    return True
            
            
def smlgrid(Sudoku):
  
    
    grid_copy == deepcopy(Sudoku)
    sym(grid_copy)
    if check_small_grid(grid_copy):    
        return True
    return False

if __name__ == '__main__':
   
    Sudoku = []
    
    for line in range(9):
       
        l = input()
        
        l = list(l)
        Sudoku.append(l)    
        
    if check1(Sudoku) and check_column(Sudoku) and check_3x3(Sudoku):
        print('Sudoku grid is valid')
    else:
        print('Sudoku grid is not valid')
  