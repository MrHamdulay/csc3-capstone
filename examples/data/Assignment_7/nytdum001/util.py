"""Module to manipulate 2 dimensional arrays
Dumisani J Nyathi
01-04-2014"""

#create a 4 by 4 grid
def create_grid(grid):
    
    grid.append([0]*4)
    grid.append([0]*4)
    grid.append([0]*4)
    grid.append([0]*4)

#print out a 4 by 4 grid in 5-width columns within a box
def print_grid (grid):
    print("+--------------------+")
    for i in grid:
        print("|",end="")
        for j in i:
            if j == 0:
                print("{:<5}".format(" "),end="")
            else:
                print("{:<5}".format(j),end="")
        print("|")
    print("+--------------------+") 
    
#return True if there are no 0 values and no adjacent values that are equal otherwise False
def check_lost (grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            if j+1<4 and grid[i][j] == grid[i][j+1]:
                return False
            if i+1<4 and grid[i][j] == grid[i+1][j]:
                return False
            if j-1>=0 and grid[i][j] == grid[i][j-1]:
                return False
            if i-1>=0 and grid[i][j] == grid[i-1][j]:
                return False
    return True

#return True if a value>=32 is found in the grid otherwise False
def check_won (grid):
    for i in grid:
        for j in i:
            if j>=32:
                return True
    return False
    pass

#return a copy of the grid
def copy_grid (grid):
    newGrid = []
    create_grid(newGrid)
    for i in range(4):
        for j in range(4):
            newGrid[i][j] = int(grid[i][j])
    return newGrid

#check if 2 grids are equal -return boolean value
def grid_equal (grid1, grid2):
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True
