#create the grid and all other utility functions to be used in 2048
#Michael Field
#27 April 2014

def create_grid(grid):
    #create a 4x4 grid
    grid = grid
    
    for i in range(4):
        grid.append([0] * 4)
    
    return grid

def print_grid(grid):
    #print out a 4x4 grid in 5-width columns within a box
    print("+--------------------+")
    
    #print the grid
    for row in range(4):
        for col in range(4):
            #format everything
            
            position = grid[row][col]
            if position == 0:
                position = " "
                
            if col == 0:
                position = '{0:<5}'.format(position)
                print('|', position,sep = "", end = "")
            
            elif col == 3:
                position = '{0:<5}'.format(position)
                print(position,'|', sep = "", end = "")
            else:    
                position = '{0:<5}'.format(position)
                print(position, sep = "", end = "")
        print()
            
    print("+--------------------+")
    
def check_lost(grid):
    lost = True
    for row in range(4):
        for col in range(4):
            
            #check for any empty spaces
            if grid[row][col] == 0:
                lost = False            
            #check for adjacent values right
            if (col+1) <= 3:
                if grid[row][col] == grid[row][col+1]:
                    lost =  False                
            
            #check for adjacent values left
            if (col-1) <= 0:
                if grid[row][col] == grid[row][col-1]:
                    lost =  False               
            
            #check for adjacent values above
            if (row-1) >= 0:
                if grid[row][col] == grid[row-1][col]:
                    lost =  False                
            
            #check for adjacent values below
            if (row+1) <= 3:
                if grid[row][col] == grid[row+1][col]:
                    lost =  False
                
    #no empty spaces and nothing can add therefore lose            
    return lost    

def check_won(grid):
    #return True if a value>=32 is found in the grid; otherwise False
    maximum = 0
    for row in range(4):
        for col in range(4):
            
            #get the maximum value of the grid
            if grid[row][col] >= maximum:
                maximum = grid[row][col]
    
    if maximum >= 32:
        return True
    else:
        return False

def copy_grid(grid):
    #create an empty grid
    copy = [[]for i in range(4)]
    
    #add the values of the current grid to the new grid
    for row in range(4):
        for col in range(4):
            copy[row].append(grid[row][col])
    
    #return the new grid which is the same as the old grid
    return copy

def grid_equal(grid1,grid2):
    #checks if 2 grids are equal
    
    for row in range(4):
        for col in range(4):
            if grid1[row][col] != grid2[row][col]:
                return False
    
    else:
        return True