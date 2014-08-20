"""Grid utility functions
Jaren Hendricks
30 April 2014"""
  
import copy
# Function to creat a 4x4 grid
def create_grid (grid):
    for i in range (4):
        grid.append ([0] * 4)
            
# Function to print the 4x4 grid
def print_grid (grid):
    print("+--------------------+")
    for i in range(4):
        print('{0:<0}'.format('|'), end='')
        if grid[i][0] == 0:
            print('{0:<5}'.format(''), end ='')
        else:
            print('{0:<5}'.format(grid[i][0]), end ='')
        for j in range(1,4):
            if grid[i][j] == 0:
                print('{0:<5}'.format(''), end ='')
            else:
                print(str(grid[i][j]).ljust(5), end = '')
        print('{0:<5}'.format('|'), end='')
        print()
    print("+--------------------+")

# function to check if there are no values and no adjacent values that are equal
def check_lost (grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
    for i in range(4):
        for j in range(3,0,-1):
            if grid[i][j]== grid[i][j-1]:
                return False
    
    for i in range(3,0,-1):
        for j in range(4):
            if grid[i][j]== grid[i-1][j]: 
                return False
    else:
        return True    

#Function to check whether a value is greater than 32
def check_won (grid):    
    for i in range(4):
        for j in range(4):
            if grid[i][j] >=32:
                return True
    else:
        return False

# Function to copy the grid
def copy_grid (grid):
    copy_grid = copy.deepcopy(grid)
    return copy_grid

# Function to check whether 2 grids are equal or not
def grid_equal (grid1, grid2):
    if grid1 == grid2:
        return True
    else:
        return False
    
            


            