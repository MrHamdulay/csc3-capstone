"""Question 2
Assignment 7
Micaela Menegaldo"""

import copy

def create_grid(grid): #working
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    return grid
                    
def print_grid(grid): #working
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in range(4):
        for column in range(4):
            if grid[row][column]==0:
                grid[row][column]=" "
            if column==0:
                print("|","{:<5}".format(grid[row][column]),sep='',end='')
            elif column==3:
                print("{:<5}".format(grid[row][column]),"|",sep='',end='')
            else:
                print("{:<5}".format(grid[row][column]),end='')
        print()
    print("+--------------------+")

def check_lost(grid): #working
    """return True if there are no 0 values and no adjacent values that are equal; otherwise return False"""
    statement=True
    for row in range(3):
        for column in range(3):
            if grid[row][column]==0:
                statement = False
            elif grid[row][column] == grid[row+1][column]:
                statement=False
            elif grid[row][column]==grid[row][column+1]:
                statement=False
                
    for column in range(3):
        if grid[3][column]==grid[3][column+1]:
            statement=False
    
    for row in range(3):
        if grid[row][3]==grid[row+1][3]:
            statement=False
    
    return statement
            
            
def check_won(grid): #working
    """return True if a value>=32 is found in the grid; otherwise False"""
    statement=False
    for row in range(4):
        for column in range(4):
            if grid[row][column]==' ' or grid[row][column]=='  ':
                grid[row][column]=0
            elif int(grid[row][column])>=32:
                statement=True
                break
    return statement
    
def copy_grid(grid): #working
    """return a copy of the grid"""
    newgrid=copy.deepcopy(grid)
    return newgrid
    
def grid_equal(grid1,grid2): #not done yet
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else:
        return False
    
    