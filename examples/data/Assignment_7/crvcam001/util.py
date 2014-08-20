# util.py
# program to manipulate 2-dimensional arrays of size 4x4
# camilla craven
# 1 may 2014

grid = []
height = 4 # 4x4 grid

def create_grid(grid):
    # create a 4x4 grid
    for i in range (height):
        grid.append ([" "] * height)    
    
    
    
def print_grid(grid):
    # print out a 4x4 grid in 5-width columns within a box
    print("+--------------------+")      
    for row in range(height):
        print("|", end = "")
        for col in range(height):          
            if grid[row][col] == 0:
                print("     ", end = "") # will print empty spaces for 0 values
            # prints value in grid with a column width of 5   
            else: print(grid[row][col],end= " "*(5 - len(str(grid[row][col]))))
        print("|", end = "")
        print()    
    print("+--------------------+")
    


def check_lost(grid):
    # return True if there are no 0 values and no adjacent values that are equal; otherwise False
    
    for row in range(height):
        for col in range(height):
            # no 0-values
            if grid[row][col] == 0:
                return False
            
    # check corner values for adjacent values that are equal       
    for row in range(height):
        for col in range(height):
            # bottom right corner
            if row == 3 and col == 3:
                if grid[row][col] == grid[row-1][col] or grid[row][col] == grid[row][col-1]:
                    return False
            # top right corner
            elif row == 0 and col == 3:
                if grid[row][col] == grid[row+1][col] or grid[row][col] == grid[row][col-1]:
                    return False
            # top left corner
            elif row == 0 and col == 0:
                if grid[row][col] == grid[row+1][col] or grid[row][col] == grid[row][col+1]:
                    return False
            # bottom left corner
            elif row == 3 and col == 0:
                if grid[row][col] == grid[row-1][col] or grid[row][col] == grid[row][col+1]:
                    return False
    
    # checking for equal adjacent values of border values that are not on the corner            
    for row in range(height):
        for col in range(height):
            # middle top two spaces of border
            if row == 0 and col == 1:
                if grid[row][col] == grid[row][col+1]:
                    return False
            # middle right two spaces of border
            elif row == 1 and col == 3:
                if grid[row][col] == grid[row+1][col]:
                    return False
            # middle bottom two spaces of border
            elif row == 3 and col == 1:
                if grid[row][col] == grid[row][col+1]:
                    return False
            # middle left two spaces of border
            elif row == 1 and col == 0:
                if grid[row][col] == grid[row+1][col]:
                    return False
                
    # checking if middle four blocks have adjacent values that are the same
    for row in range(height):
        for col in range(height):
            if row == 1 and col == 1 or row ==1 and col == 2 or row == 2 and col == 1 or row == 2 and col == 2:
                if grid[row][col] == grid[row+1][col] or grid[row][col] == grid[row-1][col] or grid[row][col] == grid[row][col+1] or grid[row][col] == grid[row][col-1]:
                    return False
            
    else: return True
            

    
def check_won(grid):
    # return True if a value >= 32 is found in the grid; otherwise False
    for row in range(height):
        for col in range(height):
            # checking each value in grid to see if bigger than 32
            if grid[row][col] >= 32:
                return True
    else: return False
    
    

def copy_grid(grid):
    # return a copy of the grid
    grid_copy = [ [], [], [], [] ]
    for row in range(height):
        for col in range(height):
            grid_copy[row].append(grid[row][col])
    return grid_copy
    
    
    
def grid_equal(grid1, grid2):
    # check if 2 grids are equal - return boolean value
    if grid1 == grid2: # checking grids are equal
        return True
    else: return False