"""Asignment 7,question 2
JT
30-04-2014"""

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])
    return grid
            
def print_grid(g):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+",'-'*20,"+",sep='')
    for i in range(len(g)):
        print('|',end='')
        for j in g[i]:
            if j == 0:
                j = ' '
            print(j,' '*(4 - len(str(j))),end='')
        print('|')
    print("+",'-'*20,"+",sep='')
    
    
        

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    value = True 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if j > 0:
                if grid[i][j] == grid[i][j-1]:
                    value = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i > 0:
                if grid[i][j] == grid[i-1][j]:
                    value = False
             
    return value
            
            
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    value = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] >= 32:
                value = True
    
    return value



def copy_grid (grid):
    """return a copy of the grid"""
    copy = []
    for i in range(len(grid)):
        copy.append([])
        for j in grid[i]:
            copy[i].append(j)
    
    return copy
    
    
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False