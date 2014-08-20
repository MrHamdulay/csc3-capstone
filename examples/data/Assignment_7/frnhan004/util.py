"""Util-assignment 7
FRNHAN004
2 May 2014"""

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (0,4):
        grid.append ([0] * 4)        
    return grid    

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+","-"* 20, "+", sep="")
    for row in range(4):
        print("|", end="")
        for col in range (4):
            if grid[row][col] == 0:
                print ("     ",end="")
            else:
                print (str(grid[row][col])+(" "*(5-len(str(grid[row][col])))),end="")        
        print("|")
    print("+","-"* 20, "+", sep="")    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    space=0
    equal=0
    for i in grid: #checking for spaces
        if 0 in i:
            space=space+1
            break
    for row in range(3,0,-1): #checking adjacent
        for num in range(2,-1,-1):
            if grid[row][num] == grid[row][num+1] or grid[row][num]==grid[row-1][num]:
                equal=equal+1
                break
            
    if space == 0 and equal == 0: #no moves left
        return True
    else:
        return False
    
          
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range (3,-1,-1):
        for num in range(3,-1,-1):
            if grid[row][num] >= 32:
                return True
    else:
        return False

def copy_grid (grid):
    """return a copy of the grid"""
    new_grid=[]
    for j in range (0,4):
            new_grid.append ([0] * 4)    
    for i in range (4): #take the block and put it there
        for k in range(4):
            new_grid[i][k] = grid[i][k]
    return new_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else:
        return False
    
    
