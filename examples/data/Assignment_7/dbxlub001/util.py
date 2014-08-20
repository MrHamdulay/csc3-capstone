"""Lubalethu Dube'
April 30 2014
grid work"""

import copy

#create 4x4 grid
def create_grid(grid):
    for i in range(4):
        listy=[]
        for j in range(4):
            listy.append(0)
        grid.append(listy)
    return grid

"""print out a 4x4 grid in 5-width columns within a box"""
def print_grid (grid):
    #print top line
    print("+--------------------+")
    for k in range(4):
        print("|",end='')
        
        for l in range (4):
            if grid [k][l]==0:
                grid[k][l]=""
                v=grid[k][l]
                print("{0:<5}".format(v),end="")
            else:
                print("{0:<5}".format(grid[k][l]),end="")
        print("|")
    #print bottom line
    print("+--------------------+")
    

"""return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
def check_lost (grid):
    #let a los == true n a not a loss equal false
    #check for spaces

    for i in range (4):
        for j in range(3):
            
           #change empty spaces into a number
            if grid[i][j]==" " or grid[i][j]=="":
                grid[i][j]=0
            #make this part be false
            if grid[i][j]==0:
                return False
            else:
                if grid[i][j+1]==grid[i][j]:
                    return False
                
    #check if adjascents are equal
    for i in range(3):
        for j in range(4):
            if grid[i+1][j]==grid[i][j]:
                return False
        

                
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    #change ' ' in 0 and find 32
    for i in range (4):
        for j in range(4):
            if grid[i][j]==" "or grid[i][j]=="":
                grid[i][j]=0
            if grid[i][j] >=32:
                return True        
    return False
            
def copy_grid (grid):
    """return a copy of the grid"""
    gridy2=[]
    gridy2=copy.deepcopy(grid)
    return gridy2

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1!=grid2:
        return False
    else:
        return True
    
    
