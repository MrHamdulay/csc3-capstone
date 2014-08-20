"""Module of grid functions
thushar hariparsad
28 april 2014"""

global grid
grid = []

def create_grid(grid):
    #create a 4x4 grid
    for y in range(4):
        row = []
        for x in range(4):
            row.append(0)
        grid.append(row)
        
def print_grid(grid):
    #print out a 4x4 grid in width-5 columns
    print("+",20*"-","+",sep="")
    for i in range(4):
        print("|",end="")
        for n in grid[i]:
            if n == 0:
                print("{0:<5}".format(" "), end="")
            else:
                print("{0:<5}".format(n), end="")
        print("|")
    print("+",20*"-","+",sep="")
    
def check_lost(grid):
    #Program to check if game is lost, returns True if there are no zero values and no adjacent values that are equal
    for i in range(4):
        for n in range(4):
            if grid[i][n] == 0:
                return False
        #search for equal horizontally adjacent values
        for n in range(3):
            if grid[i][n] == grid[i][n+1]:
                return False
    #search for equal vertically adjacent values
    for i in range(3):
        for n in range(4):
            if grid[i][n] == grid[i+1][n]:
                return False
    return True

def check_won(grid):
    #Program to determine if game is won
    #iterate through all elements in grid and return True if any values equal or greater than 32 are found
    for i in grid:
        for a in i:
            if a >= 32:
                return True
    return False

def copy_grid(grid):
    #copy of the grid
    newgrid = []
    #Loop through elements of the original grid and append to the new grid.
    for i in grid:
        new_row = []
        for a in i:
            new_row.append(a)
        newgrid.append(new_row)
    #Return the copy.
    return newgrid

def grid_equal(grid1, grid2):
    #Program to determine if two supplied grids are equal
    for i in range(4):
        for n in range(4):
            #If any corresponding values in the two grids do not match, return False.
            if grid1[i][n] != grid2[i][n]:
                return False
    #Return True if no such values are found.
    return True
            