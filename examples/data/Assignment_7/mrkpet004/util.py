"""module of utility functions to manipulate 2-dimensional arrays of size 4x4
peter m muriuki"""
import copy #import copy functions

#create a 4x4 grid
def create_grid(grid):
    height=4
    for i in range (height):
        grid.append ([0] * 4)     
        
#print out a 4x4 grid in 5-width columns within a box"""
def print_grid (grid):
    height=4
    print("+","-"*20,"+",sep="")
    for row in range (height):
        print("|",end="")
        for col in range (height): 
            f_item="{0:<5}".format(grid[row][col])
            if grid[row][col]==0:
                print(" "*5,end="")             
            else:
                print (f_item,end="")
        print("|",end="")
        print ()        
    print("+","-"*20,"+",sep="")

#return True if there are no 0 values and no adjacent values that are equal; otherwise False
def check_lost (grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==0:  
                return False
            if i>0:
                if grid[i][j]==grid[i-1][j]:
                    return False
            elif i<3:
                if  grid[i][j]==grid[i+1][j]:
                    return False
            if j>0:
                if grid[i][j]==grid[i][j-1]:
                    return False
            elif j<3:
                if grid[i][j]==grid[i][j+1]:
                    return False
    else:
        return True

#return True if a value>=32 is found in the grid; otherwise False
def check_won (grid):
    for row in range(4):
        for col in range(4): 
            if grid[row][col] >= 32:
                return True
    else:
        return False

#return a copy of the grid
def copy_grid (grid):   
    new_grid=copy.deepcopy(grid)     
    return new_grid

#check if 2 grids are equal - return boolean value
def grid_equal (grid1, grid2):
    if grid1==grid2:
        return True
    else:
        return False