#program that creates a grid

def create_grid(grid):
    for i in range (4):
        grid.append([0]*4)
    
#printing out a 4x4 grid in 5-width columns within a box
def print_grid(grid):
    print('+'+'--------------------'+'+')
    for row in range(4):
        for column in range(4):
            if grid[row][column]==0:
                grid[row][column]=' '
                
            if column==0:
                print('|'+"{0:5}".format(str(grid[row][column])),end='')
            elif column==3:
                print("{0:5}".format(str(grid[row][column]))+'|',end='')
            else:
                print("{0:5}".format(str(grid[row][column])),end='')
        print()
    print('+'+'--------------------'+'+')
    
#returning True if ther are no 0 values and no adjacent values that are equal;otherwise False
def check_lost (grid):
    #correct=False
    
    for row in range(4):
        for column in range(4):
         
            if grid[row][column]==0:
                return False
            elif column!=3 and grid[row][column]==grid[row][column+1]:
                return False
            elif row!=3 and grid[row][column]==grid[row+1][column]:
                return False
                
            #if grid[row][column]!=0 and grid[row][column]!=grid[row+1][column] and grid[row][column]!= grid[row][column+1] and grid[row][column]!=grid[row-1][column]and grid[row][column]!=grid[row][column-1]:
                #return True
            #else:
                #return False
    return True

#returning True if a value>=32 is found in the grid otherwise False
def check_won (grid):
    
    correct=False
    for row in range(4):
        for column in range(4):
            if grid[row][column]>=32:
                correct=True
    return correct        
                
#returning a copy of the grid
def copy_grid (grid):
    fresh_grid=[]
    
    for i in range (4):
        fresh_grid.append([0]*4)
        
    for row in range(4):
        for column in range(4):
            fresh_grid[row][column]=grid[row][column]
            
    return fresh_grid
    
#checking if 2 grids are equal _ return boolean value
def grid_equal (grid1,grid2):
    c=True
    for row in range(4):
        for column in range(4):
            if grid1[row][column]!=grid2[row][column]:
                c=False
    return c
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                

        
    
    
    