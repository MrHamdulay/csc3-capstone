'''Joshen Credelio Jacob
30/04/2014'''

from copy import deepcopy

grid=[]
def create_grid(grid):
    #create a 4x4 grid
    for i in range(4):
        grid.append([0]*4)

def print_grid(grid):
    #print out 4x4 grid in 5-width coulumns
    print('+--------------------+')
    for i in range(4):
        print('|',end='')
        for j in range(4):
            if grid[i][j] != 0:
                print(grid[i][j],' '*(4-len(str(grid[i][j]))),end='')
            else:
                print(' ',' '*(4-len(str(grid[i][j]))),end='')
        print('|')
    print('+--------------------+')    
    
def copy_grid(grid):
    #return a copy of the grid
    return deepcopy(grid)

def grid_equal(grid1,grid2):
    #check if the 2 grids are equal
    return grid1 == grid2

def check_lost (grid):
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False
    for i in range (4):
        for j in range (4):
            if grid[i][j]==0:   
                return False
            
            if i!=3:     
                if grid[i][j]==grid[i+1][j]:
                    return False
                
            if j!=3:     
                if grid[i][j]==grid[i][j+1]:
                    return False
    return True    

def check_won (grid):
    #return True if a value>=32 is found in the grid; otherwise False
    for i in range (4):
        for j in range (4):
            if grid[i][j]>=32:
                return True
    return False
        