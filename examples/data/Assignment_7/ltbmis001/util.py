"""Mishka Latib
code to apply util grid functions for question 2 and 2048 game, assignment 7
01 May 2014"""


grid=[]

def create_grid(grid):
    """creates a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4) 
             
def print_grid (grid):
    """prints out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in grid:
        print("|", end='')
        for j in i:
            if j==0:
                j=(" ")
            print((j)," "*(5-len(str(j))), sep='',end='')
        print("|")
    print("+--------------------+")
    
  
def check_lost (grid):
    """returns True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(3):
        for j in range(3):
            if (grid[i][0])==0 or (grid[i][0])==(grid[i][1]) or (grid[i][1])==0 or (grid[i][1])==(grid[i][2]) or (grid[i][2])==0 or (grid[i][2])==(grid[i][3]) or (grid[0][j])==(grid[1][j]) or (grid[1][j])==(grid[2][j]) or (grid[2][j])==(grid[3][j]):
                return False
        return True

def check_won (grid):
    """returns True if a value>=32 is found in the grid; otherwise False"""
    for i in grid:
        for j in i:
            if j>=32:
                return True
    return False
             

def copy_grid (grid):
    """returns copy of grid"""
    new_grid = []
    for i in grid:
        r = []
        for j in i:
            r.append(j)
        new_grid.append(r)
    return(new_grid)
    

def grid_equal (grid1, grid2):
    """checks if 2 grids are equal - returns boolean value"""
    for i in range(4):
        for j in range(4):
            if grid1[i][j]!=grid2[i][j]:
                return False
    return True
