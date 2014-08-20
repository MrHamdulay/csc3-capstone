
# A program to create util module
# Lebogang Masila
# 01 May 2014

import copy
def create_grid(grid):
    #create a 4x4 grid
    for i in range(4):
        grid.append([0]*4)
        

def print_grid (grid):
    #print out a 4x4 grid in 5-width columns within a box
    print("+"+"-"*(20)+"+",end="")
    print()
    for x in range (4):
        print("|",end="")
        for y in range(4):
            if grid[x][y] ==0:
                print("{0:<5}".format(" "),end="")
            else:    
                print("{0:<5}".format(grid[x][y]),end="")   
        print("|",end="")
        print()
    print("+"+"-"*(20)+"+",end="")
    print()
    
def check_lost (grid):
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False
    for x in range(4):
        if 0 in grid[x]:
            return False
        else:
            for y in range(4):
                if (y+1)<4 and (x+1)<4 :
                    if grid[x][y]==grid[x][y+1] or grid[x][y]==grid[x+1][y]: 
                        return False
    return True

def check_won (grid):
    #return True if a value>=32 is found in the grid; otherwise False
    for x in range(4):
        for y in range(4):
            if grid[x][y]>=32:
                return True
    return False
                
def copy_grid (grid):
    #return a copy of the grid
    copy_grid=copy.deepcopy(grid)
    return copy_grid

def grid_equal (grid1, grid2):
    #check if 2 grids are equal - return boolean value
    if grid1==grid2:
        return True
    return False    
    