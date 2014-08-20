"""More functions than I need: 4x4 array manipulation
Christopher Sterley
27/04/2014"""

import copy

def create_grid(grid):
    """create a 4x4 grid"""
    #create grid through iteration
    for create in range(4):
        grid.append([0]*4)
        

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    #print top of box
    print("+","-"*20,"+",sep="")
    
    #print sides and insides of box
    for row in range(len(grid)):
        print("|",end="")
        for column in range(4):
            if grid[row][column]==0:
                print(" "*5,end="")
                continue
            else:
                print(grid[row][column]," "*(5-len(str(grid[row][column]))),sep="",end="")
        print("|")
    
    #print bottom of box    
    print("+","-"*20,"+",sep="")    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    #variable to be changed if conditions not met
    check = True
    
    for row in range(4):
        for column in range(4):
            if grid[row][column]==0: #check for 0 values
                check = False
            if row>0:
                if grid[row][column]==grid[row-1][column]: #check if vertical adjacent values equal
                    check = False
            if column>0:
                if grid[row][column]==grid[row][column-1]: #check if horizontal adjacent values equal
                    check = False
    
    return check


def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    
    #create variable to be changed if conditions met
    won = False
    
    #check all values in grid
    for row in range(4):
        for column in range(4):
            if grid[row][column]>=32:
                won = True
    
    return won



def copy_grid (grid):
    """return a copy of the grid"""
    
    #create copy list
    copy_grid=copy.deepcopy(grid)
    
    return copy_grid



def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    
    #variable to be changed if conditions met
    equal = True
    
    #check corresponding grid values of grid1 and grid2
    for row in range(4):
        for column in range(4):
            if grid1[row][column]!=grid2[row][column]:
                equal = False
    
    return equal