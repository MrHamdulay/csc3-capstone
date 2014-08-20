'''A module of utility functions to manipulate 2-dimensional arrays of size 4x4
Daniel M. Tamale
TMLDAN001
2014-04-27'''

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    return grid   

        
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+'+'-'*20+'+')
    for i in range(4):
        grid.append([]*4)
            
    for row in range (4):
        print('|',end='')
        for col in range(4):
            if grid[row][col]==0:
                print('{0:<5}'.format(''),end='')
            else:
                print ('{0:<5}'.format(grid[row][col]),end='')
        print('|')            
    
    print('+'+'-'*20+'+')

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    lost=True
    for row in range(4):
        for col in range(4):
            if (grid[row][0]==grid[row][1]):
                lost=False
            elif (grid[row][1]==grid[row][2]):
                lost=False                
            elif (grid[row][2]==grid[row][3]):
                lost=False
                
                        
    for row in range(4):
        for col in range(4):
            if (grid[0][col]==grid[1][col]):
                lost=False
            elif (grid[1][col]==grid[2][col]):
                lost=False                
            elif (grid[2][col]==grid[3][col]):
                lost=False
                 
            
    for row in range(4):
        for col in range(4):
            if grid[row][col]==0:
                lost=False
    return lost

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won=False
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                won=True
    return won    
                    
def copy_grid (grid):
    """return a copy of the grid"""
    import copy
    new_grid=copy.deepcopy(grid)
    return new_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    a=True
    for row in range (4):
        for col in range (4):
            if grid1[row][col]!=grid2[row][col]:
                a=False
    return a