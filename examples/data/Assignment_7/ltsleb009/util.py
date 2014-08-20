#-------------------------------------------------------------------------------
# Name:        Question2
# Purpose:     Assignment 7
#
# Author:      Taylor
#
# Created:     29/05/2014
# Copyright:   (c) Taylor 2014
#-------------------------------------------------------------------------------

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0, 0, 0, 0])

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    
    print("+--------------------+")
    
    for i in range(4):
        print("|",end='')
        for j in range(4):
            if grid[i][j] == 0:
                print(' '*5,end='')
            else:
                space = 5 - len(str(grid[i][j]))
                print(grid[i][j],' '*space,sep='',end='')
        print("|")
    print("+--------------------+")
    
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    
    for i in range(4):
            if 0 in grid[i]:
                return(False)
            else:
                #check adjacant values
                for j in range(4):
                    if (j+1) < 4 and (i+1) < 4:
                        if grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i+1][j]:
                            return False
    #if both conditions are met
    return(True)    
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""

    for row in range(4): #iterates over one row at a time
        for element in grid[row]:#iterates over elements in current row
            if element >= 32:
                return(True)
    return(False)

def copy_grid (grid):
    """return a copy of the grid"""

    copy = [] #initialize new empty list

    copy.append(grid[0]) #copy all the rows from grid and append them to new list
    copy.append(grid[1])
    copy.append(grid[2])
    copy.append(grid[3])

    return(copy)

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""

    return(grid1==grid2) #check for equality