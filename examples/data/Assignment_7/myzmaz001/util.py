""" Program which contains functions that manipulate 2-D arrays
Mazwi Myeza
29 April 2014
Assignment7
Question2
"""

# Function that will create a 4x4 grid
def create_grid(grid):
    
    for i in range(4):
        grid.append([0]*4)
    #return x
# Function that will print out a 4x4 grid in 5-width columns within a box
def print_grid(grid):
    print("+--------------------+")
    for i in range(len(grid)):
        print("|", end = "")
        for j in range(len(grid)):
            if grid[i][j] == 0:
        
                print('{0:<5}'.format(" "), end = "")
            else:
                print('{0:<5}'.format(grid[i][j]), end = "")
        print("|", end = "")    
        print()    
    print("+--------------------+")        

"""Function that will return True if there are no 0 values and 
no adjacent values that are equal; otherwise False """
def check_lost(grid):
    #scrolling through grid
    for row in range(len(grid)):
        for col in range(len(grid)):
            #introducing adjacent position tracers
            left = col - 1   #left of position
            right = col + 1  #right of position
            up = row - 1     #ontop of position
            down = row + 1   #underneath position
             
            if grid[row][col] == 0: #checking if the are any 0 values
                    return False
            #Checking when position is at the bottom row       
            elif down == 4:
                    if left == -1 :
                            if grid[row][col] == grid[row-1][col]:
                                    return False
                                    
                            elif grid[row][col] == grid[row][col+1]:
                                    return False 
                                    
                    elif right == 4:
                            if grid[row][col] == grid[row-1][col]:
                                    return False
                                    
                            elif grid[row][col] == grid[row][col-1]:
                                    return False
                                    
                    else:
                            if grid[row][col] == grid[row-1][col]:
                                    return False
                                    
                            elif grid[row][col] == grid[row][col+1]:
                                    return False
                                    
                            elif grid[row][col] == grid[row][col-1]:
                                    return False
                                    
            #Checking when position is at the top row                        
            elif up == -1:
                    if left == -1 :
                            if grid[row][col] == grid[row+1][col]:
                                    return False 
                                    
                            elif grid[row][col] == grid[row][col+1]:
                                    return False
                                    
                    elif right == 4:
                            if grid[row][col] == grid[row+1][col]:
                                    return False
                                    
                            elif grid[row][col] == grid[row][col-1]:
                                    return False
                                    
                    else:
                        if grid[row][col] == grid[row+1][col]:
                            return False 
                            
                        elif grid[row][col] == grid[row][col+1]:
                            return False
                            
                        elif grid[row][col] == grid[row][col-1]:
                            return False
                            
            #Checking when position is at the first column                                
            elif left == -1:
                    if grid[row][col] == grid[row-1][col]:
                            return False
                            
                    elif grid[row][col] == grid[row][col+1]:
                            return False
                            
                    elif grid[row][col] == grid[row+1][col]:
                            return False
                            
            #Checking when position is at the last column                
            elif right ==4:
                    if grid[row][col] == grid[row-1][col]:
                            return False
                            
                    elif grid[row][col] == grid[row][col-1]:
                            return False
                            
                    elif grid[row][col] == grid[row+1][col]:
                            return False
                            
            #Checking when position is somewhere in the middle                
            else:
                    if grid[row][col] == grid[row-1][col]:
                            return False
                            
                    elif grid[row][col] == grid[row][col+1]:
                            return False
                            
                    elif grid[row][col] == grid[row][col-1]:
                            return False
                            
                    elif grid[row][col] == grid[row+1][col]:
                            return False
                            
    
    return True #returning the result

""" Fuction that will return True if a value >= 32 is found in the grid
    otherwise it will return False"""    
def check_won(grid):
    #default value
    won = False
    #checking if there is a value >= 32 in the grid
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] >= 32:
                won = True
    #returning the result            
    return won
# Function that will return a copy of the grid
def copy_grid(grid):
    #creating default grid
    copy = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    #making the default grid take on the values of the given grid
    for row in range(len(grid)):
        for col in range(len(grid)):
            copy[row][col] = grid[row][col]
    #returning the copy
    return copy        

#Function that will check if 2 grids are equal - return boolean value    
def grid_equal(grid1,grid2):
    if grid1==grid2:
        return True
    else:
        
        return False
    