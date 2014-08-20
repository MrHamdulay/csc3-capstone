# Aaron Krishna
# 02 May 2014
# 2048 grid

import copy

def create_grid(grid): #function that creates a grid
    for i in range (4):
        grid.append ([0] * 4) 
        
def print_grid (grid): #function that prints grid
    print('+--------------------+')
    for i in grid:
        print('|',end='')
        for j in i: #converts to string so that it can be validated
            j=str(j)
            if j=='0':
                print(' '.ljust(5),end='')
            else:
                print(j.ljust(5),end='')
        print('|')        
        
    print('+--------------------+')

def check_lost (grid): #function that checks if there are no 0 values and no adjacent values that are equal and returns True; else returns false
    for i in range(len(grid)):
        for j in range(len(grid) - 1):
            if grid[i][j]==0: #check if there are zeros
                return False
            elif grid[i][j]==grid[i][j+1]: #check if the value to the right equals the value
                return False
            
    for i in range(len(grid) - 1): #check if the value above equals value
        for j in range(len(grid)):    
            if grid[i][j]==grid[i+1][j]:
                return False
    else:
        return True
    
def check_won (grid): #function that checks if a value is more than 32 - therefore they have won
    for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]>=32:
                    return True
    else:
        return False

def copy_grid (grid): #function that returns a copy of the grid
    CopyGrid=copy.deepcopy(grid) #when original changes the copy doesn't
    return CopyGrid

def grid_equal (grid1, grid2): #function that checks if grids are equal
    for i in range(len(grid1)):
            for j in range(len(grid1[i])):
                if grid1[i][j]==grid2[i][j]:
                    continue
                else:
                    return False
    return True