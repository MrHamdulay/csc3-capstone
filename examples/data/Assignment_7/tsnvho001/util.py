
"""util module
Tsanwani Vhonani
30 April 2014"""

import copy

def create_grid(grid):
    #create a 4x4 grid
    for i in range(4):
        grid.append([0]*4)
        

def print_grid (grid):
    #print out a 4x4 grid in 5-width columns within a box
    corner="+"
    line="-"
    side="|"
    print(corner+line*(20)+corner,end="")
    print()
    for row in range(4):
        print(side,end="")
        for col in range(4):
            if grid[row][col] ==0:
                print("{:<5}".format(" "),end="")
            else:    
                print("{:<5}".format(grid[row][col]),end="")   
        print(side,end="")
        print()
    print(corner+line*(20)+corner,end="")
    print()
    
def check_lost (grid):
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False
    for row in range(4):
        if 0 in grid[row]:
            return False
        else:
            for col in range(4):
                if (col+1)<4 and (row+1)<4 :
                    if grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row+1][col]: 
                        return False
    return True

def check_won (grid):
    #return True if a value>=32 is found in the grid; otherwise False
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                return True
    return False
                
            

def copy_grid (grid):
    #return a copy of the grid
    copy_grid=copy.deepcopy(grid)
    return copy_grid

def grid_equal (grid1, grid2):
    #check if 2 grids are equal then return boolean value
    if grid1==grid2:
        return True
    return False    
    