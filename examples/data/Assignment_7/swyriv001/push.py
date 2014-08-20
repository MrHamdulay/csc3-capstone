""" program to simulate the game 2048
Rivoningo Seweya
01 May 2014"""
#
import copy
grid = [[4,16,2,4],[2,4,16,2],[2,4,8,4],[4,8,4,2]]
def push_up (grid):
    """merges grid values upwards"""
    #moves the block if there is a 0 value
    for i in range(3):
        for j in range(1,4):
            for k in range(4):
                if grid[j-1][k]==0 or grid[j-1]==" ":
                    grid[j-1][k] = grid[j][k]
                    grid[j][k]= 0
    #checks if adjacent blocks have the same values and adds them
    for i in range(1,4):
        for j in range(4):
            if grid[i-1][j]==grid[i][j]:
                grid[i-1][j]+=grid[i][j]
                grid[i][j]= 0   
    #moves the rest of the grid up
    for i in range(1,4):
        for j in range(4):
            if grid[i-1][j]== 0:
                grid[i-1][j] = grid[i][j]
                grid[i][j] = 0
    #if there is a value in the position
    return grid
def push_down (grid):
    """merge grid values downwards"""
    grid_new=[]
    #copy grid into new grid
    grid_new=copy.deepcopy(grid)
    #invert the original grid to get a new grid
    grid_new.reverse()
    #use push function to merge the rows
    grid_2=push_up (grid_new)
    #reverse new grid
    grid_2.reverse()
    return grid_2
def push_left (grid):
    """merge grid values left"""
    #moves the block if there is a 0 value
    for i in range(3):
        for j in range(1,4):
            for k in range(4):
                if grid[k][j-1]==0 or grid[k][j-1]==" ":
                    grid[k][j-1] = grid[k][j]
                    grid[k][j]= 0
    #checks if adjacent blocks have the same values and adds them
    for i in range(1,4):
        for j in range(4):
            if grid[j][i-1]==grid[j][i]:
                grid[j][i-1]+=grid[j][i]
                grid[j][i]= 0   
    #moves the rest of the grid up
    for i in range(1,4):
        for j in range(4):
            if grid[j][i-1]== 0:
                grid[j][i-1] = grid[j][i]
                grid[j][i] = 0
    #if there is a value in the position
    return grid
def push_right (grid):
    """merge grid values to the right"""
    grid2=[]
    grid2=copy.deepcopy(grid)
    for i in range(4):
        grid[i][0]=grid2[i][3]
        grid[i][1]=grid2[i][2]
        grid[i][2]=grid2[i][1]
        grid[i][3]=grid2[i][0]
    grid_2 = push_left(grid)
    grid_again = grid_2
    for j in range(4):
        grid[i][0]=grid2[i][3]
        grid[i][1]=grid2[i][2]
        grid[i][2]=grid2[i][1]
        grid[i][3]=grid2[i][0]
    return grid