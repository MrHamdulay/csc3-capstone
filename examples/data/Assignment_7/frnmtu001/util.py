"""This prograk creates and prints out a grid
02 may 2014"""

def create_grid(grid):
    #creates a 4x4 grid
    grid.append([0]*4)
    grid.append([0]*4)
    grid.append([0]*4)
    grid.append([0]*4)
    

def print_grid (gridz):
    #prints out a 4x4 grid in 5-width columns within a box
    print("+--------------------+")
    for i in gridz:
        print("|",end="")
        for j in i:
            if j == 0:
                print("{:<5}".format(" "),end="")
            else:
                print("{:<5}".format(j),end="")
        print("|")
    print("+--------------------+")   
def check_lost (grid3):
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False
    for i in range(4):
        for j in range(4):
            if grid3[i][j] == 0:
                return False
            if j+1<4 and grid3[i][j] == grid3[i][j+1]:
                return False
            if i+1<4 and grid3[i][j] == grid3[i+1][j]:
                return False
            if j-1>=0 and grid3[i][j] == grid3[i][j-1]:
                return False
            if i-1>=0 and grid3[i][j] == grid3[i-1][j]:
                return False
    return True
def check_won (grid):
    #return True if a value>=32 is found in the grid; otherwise False
    for i in grid:
        for k in i:
            if k>=32:
                return True
    return False
    pass
def copy_grid (grid):
    #return a copy of the grid
    newgrid = []
    create_grid(newgrid)
    for i in range(4):
        for j in range(4):
            newgrid[i][j] = int(grid[i][j])
    return newgrid
def grid_equal (grid1, grid2):
    #check if 2 grids are equal - return boolean value
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True
