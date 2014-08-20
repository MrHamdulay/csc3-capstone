"""Akhil Singh
SNGAKH004
30 April 2014"""
global grid
grid = []

def create_grid(grid):
    #Create=ing a 4x4 grid.
    for y in range(4):
        row = []
        for x in range(4):
            row.append(0)
        grid.append(row)
        
        
def print_grid(grid):
    #printing out a 4x4 grid in width-5 columns within a box.
    print("+",20*"-","+",sep="")
    for a in range(4):
        print("|",end="")
        for number in grid[a]:
            if number == 0:
                print("{0:<5}".format(" "), end="")
            else:
                print("{0:<5}".format(number), end="")
        print("|")
    print("+",20*"-","+",sep="")    
        
def check_lost(grid):
    #Check if game is lost. - Returns True if there are no zero values and no adjacent values that are equal.Otherwise returns False.
    for a in range(4):
        #Look for zero values in grid and return false if found.
        for number in range(4):
            if grid[a][number] == 0:
                return False
        #Look for equal horizontally adjacent values and return false if found.
        for number in range(3):
            if grid[a][number] == grid[a][number+1]:
                return False
    #Look for equal vertically adjacent values and return false if found.
    for a in range(3):
        for number in range(4):
            if grid[a][number] == grid[a+1][number]:
                return False
    #Return True if none of the above conditions are met.
    return True


def check_won(grid):
    #Determining if game is won. Returns True if a value >= 32 is found on the grid. Otherwise returns False.
    
    for a in grid:
        for b in a:
            if b >= 32:
                return True
    return False

def copy_grid(grid):
    #Eeturning a copy of the grid.
    #Defining a new grid.
    new_grid = []
    #check elements of the original grid and add to the new grid.
    for a in grid:
        new_row = []
        for b in a:
            new_row.append(b)
        new_grid.append(new_row)
    #Return the copy.
    return new_grid

def grid_equal(grid1, grid2):
    #Determining if two grids are equal.
    #Check all the values in each grid.
    for a in range(4):
        for number in range(4):
            #If any  values in the two grids do not match, return False.
            if grid1[a][number] != grid2[a][number]:
                return False
    #Return True if no such values are found.
    return True

