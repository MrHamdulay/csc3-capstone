#a module of utility functions to manipulate 2-dimensional arrays of size 4x4
#Jenny Luo
#30 April 2014

#create a grid
def create_grid(grid):
    """create a 4x4 grid"""
    height = 4
    for i in range (height):
        grid.append ([0] * 4)

#print out a grid within a box
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for y in range(4):
        print("|", end="")
        for x in range(4):
            if grid[y][x]==0:
                print(" "*5, end="")
            else:
                print("{0:<5}".format(grid[y][x]), end="")
        print("|")      
    print("+--------------------+")

#check if lost
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for y in range(4):
        for x in range(4):
            if grid[y][x]==0:
                return False
            elif x+1<4 and grid[y][x+1]==grid[y][x]:
                return False
            elif y+1<4 and grid[y][x]==grid[y+1][x]:
                return False
    return True

#check if win
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for y in range(4):
        for x in range(4): 
            if grid[y][x]>=32:
                return True   
    return False

#return a copy of grid
def copy_grid (grid):
    """return a copy of the grid"""
    new_grid=[]
    for y in range(4):
        Grid=[]
        for x in range(4):
            Grid.append(grid[y][x])
        new_grid.append(Grid)
    return new_grid
                
#check if 2 grids are equal
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for y in range(4):
        for x in range(4):
            if grid1[y][x]!=grid2[y][x]:
                return False
    return True
    
                
    
    
    