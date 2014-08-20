

def create_grid(grid):
    #grid = [[' ',' ',' ',' '], [' ',' ',' ',' '], [' ',' ',' ',' '], [' ',' ',' ',' ']]
    for i in range(4):
            grid.append([0]*4)    

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    
    #loop through each row in 2d grid array
    for row in range(4):
        count = 0
        print("|", end="")
        #loop through each column in grid array and print item (0 printed as ' ')
        for col in grid[row]:
            if (col != 0):
                #align items to rigth by 5 places
                print('{:<5}'.format(grid[row][count]), end="")
            else:
                print('{:<5}'.format(" "), end="")
            count+=1
        print("|")
    print("+--------------------+")   
                

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    #loop through every item in grid            
    for row in range(4):
            for col in range(4):
                
                if(grid[row][col]==0):
                    return False
                #check if adjacent items are equal(except corners)
                elif(row!=0 and row!=3 and col!=0 and col!=3):
                    if(grid[row][col]==grid[row][col-1] or grid[row][col]==grid[row-1][col] or grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row+1][col]):
                        return False
                #check 4 corners:
                elif(grid[0][0]==grid[0][1]or grid[0][0]==grid[1][0]):
                    return False
                elif(grid[0][3]==grid[0][2]or grid[0][3]==grid[1][3]):
                    return False   
                elif(grid[3][0]==grid[3][1]or grid[3][0]==grid[2][0]):
                    return False   
                elif(grid[3][3]==grid[3][2]or grid[3][3]==grid[2][3]):
                    return False                
                
    return True
                
                ##check if any zeroes
                #if(grid[i][j]==0):
                    #return False
                ##end of grid = return true
                #elif (i==3 and j==3):
                    #return True
                #elif (i==3):
                    #if((grid[i][j]==grid[i][j+1])):
                        #return False
                #elif (j==3):
                    
                    #if(grid[i][j]==grid[i+1][j]):
                        #return False
                    
                #elif(grid[i][j]==grid[i+1][j] or grid[i][j]==grid[i][j+1]):
                    #return False

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    #loop through entire grid
    for row in range(4):
        for col in range(4):
            #check if value >= 32
            if(grid[row][col] >= 32):    
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    newGrid = []
    #loop through grid
    for row in range(4):
        newRow = []
        for col in range(4):
            #add items to newrow
            newRow.append(grid[row][col])
        #add row to the new grid
        newGrid.append(newRow)    
    return newGrid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    #loop through grid1 and check if each item is the same as grid2
    for row in range(4):
        for col in range(4):
            if (grid1[row][col]!=grid2[row][col]):
                return False
    return True
                