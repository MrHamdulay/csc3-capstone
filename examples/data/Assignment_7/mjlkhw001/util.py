# 2D Array manipulator
# Khwezi Majola
# MJLKHW001
# 27 April 2014

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4) 
    return grid
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+' + '-'*20 + '+')
    for i in range(4):
        print('|', end='')
        for j in range(4): #Loop through every entry
            if grid[i][j] == 0: 
                output = '{0:<5}'.format('') #Make 0 output as an empty space
            else: output = '{0:<5}'.format(grid[i][j]) #Output the number in the correct format
            print(output, end='')
        print('|', end='\n')
    print('+' + '-'*20 + '+')
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            if 0 <= i+1 <= 3: #Test if the list index will exist
                if grid[i+1][j] == grid[i][j]: #Checks if adjacant values are equal
                    return False
            if 0 <= i-1 <= 3: #Test if the list index will exist
                if grid[i-1][j] == grid[i][j]: #Checks if adjacant values are equal
                    return False
            if 0 <= j+1 <= 3: #Test if the list index will exist
                if grid[i][j+1] == grid[i][j]: #Checks if adjacant values are equal
                    return False
            if 0 <= j-1 <= 3: #Test if the list index will exist
                if grid[i][j-1] == grid[i][j]: #Checks if adjacant values are equal
                    return False 
    return True #Only returns true if none of the above conditions are met
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32: #Tries to find 32 and return True or False
                check = True
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    import copy
    copy_grid = copy.deepcopy(grid) #Makes use of deepcopy from the copy module
    return copy_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]: #Checks if they aren't equal to end the loop and return False
                return False
    return True   