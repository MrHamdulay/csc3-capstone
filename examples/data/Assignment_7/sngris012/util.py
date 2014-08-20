#Rishen Singh SNGRIS012 Assignment7

def create_grid (grid): 
    for i in range(4):
        grid.append([0,0,0,0]) #creates 4x4 grid and assigns every item in grid to 0
    return grid

def print_grid(grid): #prints grid in the 5 column box
    print("+--------------------+")
    
    for i in range(4):
        print("|",end="")
        for j in range(4):
            if(grid[i][j]==0):
                print("{:<5}".format(" "),end="")
            else:
                print("{:<5}".format(grid[i][j]),end="") #formats the output of the grid to fit in the box
        print("|",end="")    
        print()
    print("+--------------------+")



def check_won (grid):
    for i in range(4):
        for j in range(4):
            if(grid[i][j]>=32): #checks if there is a value within grid that is greater than 32 and returns True to show you have won
                return True
    return False

def check_lost(grid):
    for k in range(4):
        for j in range(4):
            if(grid[k][j]==0): #checks if there are any 0 values within grid, if not, and there are no adjacent values that are equal as well, returns true to show that you lost.
                return False
            if(j<3 and grid[k][j]==grid[k][j+1]): #checks if adjacent values are equal
                return False
            if(k<3 and grid[k][j]==grid[k+1][j]):
                return False
    
    return True

def copy_grid(grid):
    copy=[['','','',''],['','','',''],['','','',''],['','','','']] 
    for i in range(4):
        for j in range(4):
            copy[i][j]=grid[i][j] #copies the elements from the paramter grid into a new grid, and returns that grid
    return copy

def grid_equal (grid1, grid2): #checks if two grids are equal.
    if(grid1==grid2):
        return True
    else:
        return False
            
            
    



                