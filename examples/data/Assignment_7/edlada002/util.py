"""push
Adam Edelberg
2014/04/29"""

def create_grid(grid):
    """create a 4x4 grid"""
    blank_array = [0,0,0,0]
    for i in range (4):
        grid.append (blank_array[:])
      
    

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in range (4):
        print("|",end="")
        for col in range (4):
            if grid[row][col] == 0:
                print("     ",end="")
            else:
                print ("{0:<5}".format(grid[row][col]),sep="", end="")
        print("|",end="")
        print()
    print("+--------------------+")
    
        
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    zero=False
    adjacent=False
    for row in range (4):
        for col in range (4):    
            if grid[row][col] == 0:
                zero=True
    for row in range (3):
        for col in range (3):
            if grid[row][col] == grid[row][col+1]:
                adjacent = True
            if grid[row][col] == grid[row+1][col]:
                adjacent = True
    if (zero == False and adjacent == False):
        return True
    return False
                
               
    

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range (4):
        for col in range (4):
            if grid[row][col] >= 32:

                return True
    return False
  

def copy_grid (grid):
    """return a copy of the grid"""
    import copy
    grid2 = copy.deepcopy(grid)   
    return grid2
    

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    return False 
                
    
