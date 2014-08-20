"""utility functions
Michelle Lu
27 April 2014"""
import copy
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)

    
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in range(4):
        for col in range(6):
            if col==0:
                print("|", sep="", end="")
            elif 1<=col<5:
                if grid[row][col-1]==0:
                    print("{0:<5}".format(" "), sep="", end="")
                else: 
                    print("{0:<5}".format(grid[row][col-1]), sep="", end="")
                    
            else:
                print("|", sep="")
    print("+--------------------+")
    
def check_lost(grid):
    x = True
    for row in range(4): 
        for col in range(4):
            left= col-1    #check if value on either side of number is the same
            right=col+1
            top=row-1
            bottom=row+1            
            
            if grid[row][col]==0: #check if value is equal to 0
                return False
            
            elif row==0 and col==0: #top left
               
                if grid[row][col]==grid[row][right] or grid[row][col]==grid[bottom][col]:
                    return False
           
            elif row==0 and col==3: #top right
                if grid[row][col]==grid[row][left] or grid[row][col]==grid[bottom][col]:
                    return False         
            
            elif row==3 and col==0: #bottom left
                if grid[row][col]==grid[row][right] or grid[row][col]==grid[top][col]:
                    return False         
            
            elif row==3 and col==3: #bottom right
                if grid[row][col]==grid[row][left] or grid[row][col]==grid[top][col]:
                    return False        
            
            elif col==0:
                if grid[row][col]==grid[row][right] or grid[row][col]==grid[bottom][col] or grid[row][col]==grid[top][col]:
                    return False              
            
            elif col==3:
                if grid[row][col]==grid[row][left] or grid[row][col]==grid[bottom][col] or grid[row][col]==grid[top][col]:
                    return False       
            
            elif row==0:
                if grid[row][col]==grid[row][right] or grid[row][col]==grid[bottom][col] or grid[row][col]==grid[row][left]:
                    return False         
                    
            elif row==3: 
                if grid[row][col]==grid[row][right] or grid[row][col]==grid[top][col] or grid[row][col]==grid[left][col]:
                    return False
            
            elif grid[row][col] == grid[row][left] or grid[row][col] == grid[row][right] or grid[row][col] == grid[top][col] or grid[row][col] == grid[bottom][col]:
                return False


    return x


def check_won(grid):
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                return True
    return False

def copy_grid(grid):
    box=copy.deepcopy(grid)
    return box

def grid_equal (grid1, grid2):
    count =0
    for row in range(4):
        for col in range(4):
            if grid1[row][col]==grid2[row][col]:
                count+=1
    if count==16:
        return True
    else:
        return False
            
            