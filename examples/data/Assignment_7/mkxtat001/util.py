#Tato Moaki MKXTAT001
#Module of functions to manipulate 2-D arrays of size 4 x 4
#Assignment7 question2

def create_grid(grid):
    """create a 4x4 grid"""    
    for i in range(4):        
        grid.append([0] * 4) #create a list of size 4 and append to grid to create a 2-D array
    return(grid)   

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+") 
    for row in range(4):
        print("|",end="")
        for column in range(4):
            if (grid[row][column] == 0):
                print("{0:<5}".format(" "),end="")#left align grid[row][column] in width of 5
            else:
                print("{0:<5}".format(grid[row][column]),end="")
        print("|")    
    print("+--------------------+")
    
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for column in range(4):
            if grid[row][column] >= 32:
                return True
    else:    
        return False

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range(3):
        for column in range(3):
            if grid[row][column] == grid[row][column+1] or grid[row][column] == grid[row+1][column] or grid[row][column]== 0:
                return False
    else:
        return True                
            
def copy_grid (grid):
    """return a copy of the grid""" 
    grid_copy = []
    for element in grid:
        grid_copy.append(list(element))
        
    return grid_copy


def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    return False