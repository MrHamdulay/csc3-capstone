#perform different functions on grids
#romelon chetty(chtrom001)
#30 april 2014



grid=[]
def create_grid(grid):
    for i in range (4):
        grid.append([0]*4) # attach a 1 by 4 array to bigger array to create 4 by 4
    return grid

def print_grid (grid):
    print('+--------------------+') 
    for i in range(4):
        print('|', end='') 
        for j in range(4):
            if grid[i][j]==0:
                print(' '*5, end='') #replaces the 0 with 5 spaces 
            else:
                print(grid[i][j], (5-len(str((grid[i][j]))))*' ', sep='', end='') #Print out value and subtract the characters from the string of the value to work out number of spaces to print.
        print('|')
    print('+--------------------+')
    
def check_lost (grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0: #if there is a space,then game continues
                return False
            
            if j!=3:
                if grid[i][j]==grid[i][j+1]: #checks whether values are in grid
                    return False
            if i!=3:
                if grid[i][j]==grid[i+1][j]: #Checks whether values are in grid
                    return False
         
                
    return True    
                            

def check_won (grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32: #If a position is greater than or equal to 32,then you win
                return True
    return False

def copy_grid (grid):
    full_grid=[]
    
    for i in range(4):
        new_grid=[]
        for j in range(4):
            new_grid.append(grid[i][j]) #create each row
        full_grid.append(new_grid) #add the row to the new grid
    return full_grid
            
            
            
        
        
    

def grid_equal (grid1, grid2):
    for i in range(4):
        for j in range(4):
            if grid1[i][j]!=grid2[i][j]: #checks if two grids are equal
                return False
    return True