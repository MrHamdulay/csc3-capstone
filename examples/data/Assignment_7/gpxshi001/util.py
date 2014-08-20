#GPXSHI001
#Ass7
#q2 "util"

global grid
grid = []

def create_grid(grid):
    """Program to create a 4x4 grid."""
    
    for y in range(4):
        hor = []
        for x in range(4):
            hor.append(0)
        grid.append(hor)
        
def print_grid(grid):
    """Program to print out a 4x4 grid in width-5 columns within a box."""
    
    print("+",20*"-","+",sep="")
    for i in range(4):
        print("|",end="")
        for num in grid[i]:
            if num == 0:
                print("{0:<5}".format(" "), end="")
            else:
                print("{0:<5}".format(num), end="")
        print("|")
    print("+",20*"-","+",sep="")
    
def check_lost(grid):
    """Program to check if game is lost. - Returns True if there are no zero values and no adjacent values that are equal.
    Otherwise returns False."""
    
    for i in range(4):
        for num in range(4):
            if grid[i][num] == 0:
                return False
            
        for num in range(3):
            if grid[i][num] == grid[i][num+1]:
                return False
    
    for i in range(3):
        for num in range(4):
            if grid[i][num] == grid[i+1][num]:
                return False
    return True

def check_won(grid):
    """Program to determine if game is won. Returns True if a value >= 32 is found on the grid. Otherwise returns False."""
    for i in grid:
        for a in i:
            if a >= 32:
                return True
    return False

def copy_grid(grid):
    """Program that returns a copy of the grid."""
    new_grid = []
    
    for i in grid:                       #to create a copy of the grid
        new_hor = []
        for a in i:
            new_hor.append(a)
        new_grid.append(new_hor)
        
    return new_grid

def grid_equal(grid1, grid2):
    """Program to determine if two supplied grids are equal."""

    for i in range(4):
        for num in range(4):
            if grid1[i][num] != grid2[i][num]:
                return False
    return True
            