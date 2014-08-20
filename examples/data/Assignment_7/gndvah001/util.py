"""grid thingy
Vahin Gounden
27-04-2014"""

def create_grid(grid):
    """create a 4x4 grid"""
    grid = grid
    for i in range (0,4):
        grid.append ([0,0,0,0])
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    #grid = [[" "for j in range(4)] for j in range(4)]
    grid = grid
    for i in range (0,4):
        for j in range (0,4):
            if grid[i][j] == 0:
                grid[i][j] = " "
    print ("+--------------------+")
    print ("|","{0: <5}".format(grid[0][0]),"{0: <5}".format(grid[0][1]),"{0: <5}".format(grid[0][2]),"{0: <5}".format(grid[0][3]),"|",sep = "") 
    print ("|","{0: <5}".format(grid[1][0]),"{0: <5}".format(grid[1][1]),"{0: <5}".format(grid[1][2]),"{0: <5}".format(grid[1][3]),"|",sep = "")
    print ("|","{0: <5}".format(grid[2][0]),"{0: <5}".format(grid[2][1]),"{0: <5}".format(grid[2][2]),"{0: <5}".format(grid[2][3]),"|",sep = "")
    print ("|","{0: <5}".format(grid[3][0]),"{0: <5}".format(grid[3][1]),"{0: <5}".format(grid[3][2]),"{0: <5}".format(grid[3][3]),"|",sep = "")
    print ("+--------------------+")
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    grid = grid    
    sme = 0
    z = 0
    for i in range(3):
        for j in range(1,4):
            if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i+1][j]:
                sme+=1
                break
    #see if there are zeros
    for i in range(4):
        if 0 in grid[i]:
            z+=1
            break
    if sme==0 and z==0:
        return True
    else:
        return False
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""   
    grid = grid
    w = 0
    for i in range (0,4):
        for j in range (0,4):
            if grid[i][j] >=32:
                w = w + 1
                break   
    
    if w == 0:
        return False
    else:
        return True  
    
def copy_grid (grid):
    """return a copy of the grid"""
    grid = grid
    duplicate = []
    for i in range(4):
        duplicate.append([0]*4)
    for i in range(4):
        for s in range(4):
            duplicate[i][s] = grid[i][s]
    return duplicate    
    
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False    