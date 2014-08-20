'''a module of utility functions to manipulate 2-dimensional arrays of size 4x4
fadzai mupfunya
29/04/14'''
import copy
#a 4x4 grid
def create_grid(grid):
    for i in range (4):
        grid.append ([0] * 4)


#to print out a 4x4 grid in 5-width columns within a box
def print_grid (grid):    
    print("+--------------------+")         
    for row in range (4):
        print("|", end='')
        for col in range (4):
            if grid[row][col]==0:
                print(" "*5, end='')
            else:
                print ('{0:<5}'.format(grid[row][col]),end='') #to make the 5-width columns
        print("|", end='')
        print ()  
    print("+--------------------+")
    
def check_lost (grid):       #returns True if there are no 0 values and no adjacent values that are equal; otherwise False
    for row in range (4):
            for col in range (4):
                    if grid[row][col]==0:
                        return False
                    elif col!=3 and grid[row][col]==grid[row][col+1]: #to make sure loop does not include the fourth column
                        return False
                    elif row!=3 and grid[row][col]==grid[row+1][col]:
                        return False
                   
                                
    
    return True
     
           
def check_won (grid):       #returns True if a value>=32 is found in the grid; otherwise False
    for row in range (4):
            for col in range (4):
                if grid[row][col] >= 32:
                    return True                                       
    else:
        return False
        print ()  

def copy_grid (grid):    #returns a copy of the grid
    return copy.deepcopy(grid)
    
def grid_equal (grid1, grid2):  #to check if two grids are equal
    if grid1 == grid2:
        return True
    else:
        return False
   
    

    
    