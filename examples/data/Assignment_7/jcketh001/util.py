#Program to manipulate a 4x4 array
#Ethan Jackson 
#28 April 2014

def create_grid(grid):
    #create a 4x4 grid
    for i in range(4):                          
        grid.append([0,0,0,0])                  
    return grid                                 

def print_grid (grid):
    #print 4x4 grid in 5-width columns inside a box
    print("+--------------------+")             
    for i in range(4):                          
        string = '|'                              
        for j in range(4):                      
            value = str(grid[i][j])               
            if value == '0':
                value = ' '                       
            string += value + ' ' * (5-(len(value)))  
        string += '|'                            
        print(string)                           
    print("+--------------------+") 
    
def check_lost(grid):
    #Returns true if no 0 values,else it returns false
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                return False
            elif i+1 < len(grid):
                if grid[i][j] == grid[i+1][j]:
                    return False
            elif j+1 < len(grid[i]):
                if grid[i][j] == grid[i][j+1]:
                    return False            
    return True

def check_won(grid):
    #Returns true if values found in grid are greater than or equal to 32, else it returns False
    for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] >= 32:
                    return True    
    return False

def copy_grid(grid):
    #Returns a copy of the grid
    new_grid = []
    new_grid = create_grid(new_grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_grid[i][j] = grid[i][j]
    return new_grid

def grid_equal (grid1, grid2):
    #returns true if the grids are equal
    if grid1 == grid2:                            #checks to see if grids are the same
        return True
    else:
        return False