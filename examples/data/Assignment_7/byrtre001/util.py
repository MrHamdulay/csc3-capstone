"""grid utility functions
Trevor Byaruhanga
03 May 2014"""

#create an empty list
grid=[]
#create a grid 
def create_grid(grid):
    height=4
    #create a 4x4 grid
    for i in range (height):
        grid.append ([0] * 4)  
        
    return grid


def print_grid (grid):
    height=4
    print('+--------------------+')
    #"""print out a 4x4 grid in 5-width columns within a box
    for row in range (height):  
        if row>=0:
            print('|',end='')
        for col in range (height):
            #if 0's a value, print a space instead of the value 0
            if grid[row][col]==0:
                print(' ',' '*((height+1)-len(str(grid[row][col]))),end='',sep='')
            else:
                print (grid[row][col],' '*((height+1)-len(str(grid[row][col]))),end='',sep='')
            
        print('|')
    print('+--------------------+')
#print_grid (create_grid(grid)) This function prints the values in the grid
def check_lost (grid):
    height=4
    
    for row in range (height):  
        for col in range (height):
            if grid[row][col]==0: 
                return False
            else:
                continue
    for row in range (3):  
        for col in range (height):
            if grid[row][col]==grid[row+1][col]:
                return False
            else:
                continue
    for row in range (height):  
        for col in range (3):
            if grid[row][col]==grid[row][col+1]:
                return False
            else:
                continue    
    return True
  
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False

def check_won (grid):
    height=4
    for row in range (height):  
            for col in range (height):
                if grid[row][col]:
                    if grid[row][col]>=32: 
                        return True
                    else:
                        continue
        
    return False
#return True if a value>=32 is found in the grid; otherwise False

def copy_grid (grid):
    height=4
    """create a 4x4 grid"""
    for i in range (height):
        grid.append ([0] * 4)
    return print_grid ((grid))
      
#"""return a copy of the grid"""
    
def grid_equal (grid1, grid2):
    height=4
    
    for row in range (height):  
        for col in range (height):
            if grid1[row][col]==grid2[row][col]: 
                return True
            else:
                continue
        
    return False   
    
#check if 2 grids are equal - return boolean value