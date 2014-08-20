"""module of utility functions
Jacqueline Blomendahl
30 April 2014"""

def create_grid(grid):
    """create a 4x4 grid"""
    height = 4
    
    for i in range (height):
        grid.append([0,0,0,0])
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range(4):
        print("|", end='')
        for k in range (4):
            if grid[i][k]==0:
                print("{0:<5}".format(" "), end='')
            else:
                print("{0:<5}".format(grid[i][k]), end='')
        print("|")
    print("+--------------------+")
    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    if (0 in grid):
        return False
    
    for i in range(4):
        for k in range(4):
            if k!=0:
                if grid[i][k-1]==grid[i][k]: #checking to left
                    return False
            if k!=3:
                if grid[i][k+1]==grid[i][k]:  #checking to right
                    return False
            if i!=0:
                if grid[i-1][k]==grid[i][k]:   #checking above
                    return False
            if i!=3:
                if grid[i+1][k]==grid[i][k]:   #checking below
                    return False
    else:
        return True
            
                    

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:        #checking for a 32 or higher
                return True
    else:
        return False

def copy_grid (grid):
    """return a copy of the grid""" # import copy    return copy.deepcopy(grid)
    newgrid=[]
    for j in range (4):
        newgrid.append([])  #adding the collumns to newgrid
        for x in range (4):
            newgrid[j].append(grid[j][x])    #adding the values of the row to the collumn of newgrid
    return newgrid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else:
        return False 