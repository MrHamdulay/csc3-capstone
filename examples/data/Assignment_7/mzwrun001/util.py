"""module with functions to manipulate 2-d arrays
Runako Muzwidzwa
29/04/2014"""
import copy
#to create a 4x4 grid
grid = [[2,16,4,2],[4,8,64,4],[2,4,8,2],[4,8,2,4]]
def create_grid(grid):
    height=4
    for i in range(height):
        grid.append([0]*4)

#to print out a 4x4 grid in 5-width columns within a box
def print_grid(grid):
    print("+","-"*20,"+",sep="")       
    for row in range (4):
        print("|",end="")
        for col in range (4):
            if grid[row][col]==0:
                print(" "*5,end="")
            else:
                print ("{0:<5}".format(grid[row][col]),end="",sep="") 
        print("|",end="")
        print ()
    print("+","-"*20,"+",sep="")

#return true if there are no 0 values and no adjacent values 
def check_lost (grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col]==0:
                return "False"
            elif grid[row][col]==grid[row][col+1]:
                return "False"
            elif grid[row][col]==grid[row+1][col]:
                return "False"
    else:
            return "True"
#check if game is lost
def check_won(grid):
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                return "True"
    else:
                return "False"

#return a copy of grid
def copy_grid(grid):
    copy_grid=copy.deepcopy(grid)
    return copy_grid
    

#check if 2 grids are equal
def grid_equal(grid1,grid2):  
    for row in range (4):
        for col in range (4):
            
            if grid1[row][col] != grid2[row][col]:
                return "False"
    else:
                return "True"
        