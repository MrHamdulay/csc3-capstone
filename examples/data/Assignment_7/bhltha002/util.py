#Thabang Bhili
#02/05/2014
#A program to create grids for question 3

grid = []
height = 4

#Creating a 4x4 Grid
def create_grid (grid):
    """Creates a 4x4 grid""" 
    
    for i in range (height):
        #Adding list ['','','',''] to grid
        grid.append ([0] * height)
    

#Print a 4x4 grid with column width 5
def print_grid (grid):
    """Prints a 4x4 grid"""
    
    #Printing border
    print ("+--------------------+")
    for i in range (height):
        print ("|",end='')
        for j in range (height):
            if grid [i][j] != 0:
                print (str (grid [i][j]) + (5-len(str(grid [i][j])))*' ', end = '')
            else:
                print ('     ', end = '')
        print ("|")
    print ("+--------------------+")
    
#Checking if the game has been lost
def check_lost (grid):
    """Checks for no 0 and no identical adjacent number in entire grid"""
    
    #Assume player has lost
    lost = True
    last = 3
    
    #Checking if values below and to the right of current location are the same
    for i in range (height):
        if i == 0:
            for j in range (height - 1):
                if grid [i][j] == grid [i][j+1] or grid [i][j] == grid[i+1][j]:
                    return False
        elif i == 1:
            for j in range (height - 1):
                if grid [i][j] == grid [i][j+1] or grid [i][j] == grid[i+1][j]:
                    return False
        elif i == 2:
            if grid [i][j] == grid [i][j+1] or grid [i][j] == grid[i+1][j]:
                return False
        elif i == 3:
            for j in range (height - 1):
                if grid [i][j] == grid [i][j+1]:
                    return False
                
    #Performing check in last column            
    for i in range (height - 1):
        if grid [i][last] == grid [i+1][last]:
            return False
        
    #Checking for ['']
    for i in range (height):
        for j in range (height):
            if grid [i][j] == 0:
                return False
    
    return lost
               
#Checking if the game has been won
def check_won (grid):
    """Checks for the number 32"""
    
    for i in range (height):
        for j in range (height):
            if grid [i][j] >= 32:
                return True
            
    return False
    
#Creating a copy of the grid
def copy_grid (grid):
    """Creates a copy of the grid"""
    
    new_grid = []
    #Creating new grid
    create_grid (new_grid)
    for i in range (height):
        for j in range (height):
            new_grid [i][j] = grid [i][j]
            
    return new_grid
    
#Checking if two grids are equal
def grid_equal (grid1, grid2):
    """Compares 2 grids"""
    
    #Assumed to be True
    result = True
    for i in range (height):
        for j in range (height):
            if grid1 [i][j] != grid2 [i][j]:
                result = False
                
    return result
                
