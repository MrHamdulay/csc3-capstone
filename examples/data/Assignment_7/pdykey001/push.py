"""
Keyoolin Padayachee
Push Functions
01 May 2014
"""


#imports the util class
import util
#Push all values in the grid up
def push(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0 and i != 3:
                if grid[i+1][j] == 0 and i !=2:
                    if grid[i+2][j] == 0 and i !=1:
                        grid[i][j],grid[i+3][j] = grid[i+3][j],grid[i][j]
                    else: grid[i][j],grid[i+2][j] = grid[i+2][j],grid[i][j]
                else : grid[i][j],grid[i+1][j] = grid[i+1][j],grid[i][j]
    return grid
#Merge values in the grid that are adjacent                
def merge(grid):                        
    for i in range(4):
        for j in range(4):
            if i !=3 and grid[i+1][j] == grid[i][j]:
                grid[i][j],grid[i+1][j] = grid[i][j]*2,0
                
    return grid
#Rotates the grid 180 degrees to make the push function usable when needing to push down
def rotate180(grid):
    gridcopy = util.copy_grid(grid)
    for i in range(4):
        for j in range(4):
            grid[i][j] = gridcopy[3-i][j]
    return grid
#Rotates the grid 90 degrees to the right
def rotate90r(grid):
    gridcopy = util.copy_grid(grid)
    for i in range(4):
        for j in range(4):    
            grid[i][j] = gridcopy[3-j][i]
    return grid
#rotates the grid 90 degrees to the left
def rotate90l(grid):
    gridcopy = util.copy_grid(grid)
    for i in range(4):
        for j in range(4):    
            grid[i][j] = gridcopy[j][3-i]    
    return grid
#Calls the required functions to push up grid
def push_up(grid):
    push(grid)
    merge(grid)
    push(grid)
    return(grid)
#Calls the required functions to push down grid
def push_down(grid):
    rotate180(grid)
    push_up(grid)
    rotate180(grid)
    return grid
#Calls the required functions to push left grid
def push_left(grid):
    rotate90r(grid)
    push_up(grid)
    rotate90l(grid)    
    return grid
#Calls the required functions to push right grid
def push_right(grid):
    rotate90l(grid)
    push_up(grid)
    rotate90r(grid)   
    return grid