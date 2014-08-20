#ass.7 Q2 2048
#Kavir Ranchod RNCKAV001
#03/05/2014

global grid
grid = []

def create_grid(grid):
    """Program to create a 4x4 grid."""
    for i in range(4):
        row = []
        for j in range(4):
            row.append(0)
        grid.append(row)
        
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
        #Checks for 0 values
        for num in range(4):
            if grid[i][num] == 0:
                return False
        #Checks for no equal horizontally adjacent values
        for num in range(3):
            if grid[i][num] == grid[i][num+1]:
                return False
    #Checks for no equal vertically adjacent values
    for i in range(3):
        for num in range(4):
            if grid[i][num] == grid[i+1][num]:
                return False
    #return true if none of the above conditions are met
    return True

def check_won(grid):
    """Program to determine if game is won. Returns True if a value >= 32 is found on the grid. Otherwise returns False."""
    #Checks entire grid for values greater than or equal to 32
    for i in grid:
        for a in i:
            if a >= 32:
                return True
    return False

def copy_grid(grid):
    """Program that returns a copy of the grid."""
    #Create a new empty grid
    new_grid = []
    #Transfer values from old grid into new grid
    for i in grid:
        new_row = []
        for a in i:
            new_row.append(a)
        new_grid.append(new_row)
    #Return new version of the grid
    return new_grid

def grid_equal(grid1, grid2):
    """Program to determine if two supplied grids are equal."""
    for i in range(4):
        for num in range(4):
            #Checks if any values match in both grids, and returns false if there are
            if grid1[i][num] != grid2[i][num]:
                return False
    return True