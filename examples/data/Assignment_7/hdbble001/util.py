def create_grid(grid):
    """create a 4x4 grid"""
    for row in range(4):
        temp=[]
        for column in range(4):
            temp.append(0) #adds a 0 to the temporary array temp with each iteration
        grid.append(temp) #adds the array temp to the array grid
    return grid #returns a 4x4 array

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in grid:
        print("|", end="")
        for column in row:
            if column==0:
                column="" #prints nothing if the current value in the grid is 0
            print("{0:<5}".format(column), end="") #prints any non-zero values in a column of width 5, left justified
        print("|", end="")
        print()
    print("+--------------------+")
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range(4):
        for column in range(4):
            if grid[row][column]==0:
                return False #returns False if there is a 0 value in grid
            elif column>=0:
                if grid[row][column]==grid[row][column-1]:
                    return False #returns False if value to the left is equal
            elif column<=3:
                if grid[row][column]==grid[row][column+1]:
                    return False #returns False if value to the right is equal
            elif row>=0:
                if grid[row][column]==grid[row-1][column]:
                    return False #returns False if value above is equal
            elif row<3:
                if grid[row][column]==grid[row+1][column]:
                    return False #returns False if value below is equal
    return True #returns True if there are no 0 values and no adjacent values that are equal

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for column in range(4):
            if grid[row][column]>=32:
                return True #return True if a value>=32 is found in the grid
    return False    #return False if all values are <32

def copy_grid (grid):
    """return a copy of the grid"""
    newgrid=[]
    for row in range(4):
        temp=[]
        for column in range(4):
            temp.append(grid[row][column]) #adds a value from original grid to the temporary array temp with each iteration
        newgrid.append(temp) #adds the array temp to newgrid
    return newgrid #returns a copy of the original grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for row in range(4):
        for column in range(4):
            if grid1[row][column] != grid2[row][column]: #checks if each value of grid1 is equal to the value in the same position in grid2
                return False #returns False if any grid1 values are not equal to the corresponding grid2 value
    return True #returns True if grid1 and grid2 are equal