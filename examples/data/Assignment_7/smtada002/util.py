'''Assignment 7 question 2 Grid creator and checker
Adam Smith
27 April 2014'''

def create_grid(grid): #create a 4x4 grid
    y1list = []
    y2list = []
    y3list = []
    y4list = []
    for i in range (4):
        y1list.append(0)
        y2list.append(0)
        y3list.append(0)
        y4list.append(0)
        
    grid.append(y1list)
    grid.append(y2list)
    grid.append(y3list)
    grid.append(y4list)
    
    return grid

def print_grid (grid): #print out a 4x4 grid in 5-width columns within a box
    print("+--------------------+")
    
    for i in range(4):
        print("|", end = "")
        for j in range (4):
            if grid[i][j] != 0:
                print('{0:<5}'.format(grid[i][j]), end = "")
            else:
                print("     ", end = "")
        print("|")
        
    print("+--------------------+")
        
    
def check_lost (grid): #return True if there are no 0 values and no adjacent values that are equal; otherwise False
    Has_Lost = True
    
    for i in range(4):
        for j in range (4):
                
            if grid[i][j] == 0:
                Has_Lost = False
            
            elif i > 0 and i < 3:
                if grid[i - 1][j] == grid[i][j] or grid[i + 1][j] == grid[i][j]:
                    Has_Lost = False
            
            elif j > 0 and j < 3:
                if grid[i][j - 1] == grid[i][j] or grid[i][j + 1] == grid[i][j]:
                    Has_Lost = False
                    
            
                
    return Has_Lost 

def check_won (grid): #return True if a value>=32 is found in the grid; otherwise False
    
    for i in range(4):
        for j in range (4):
            if grid[i][j] >= 32:
                return True
    return False

def copy_grid (grid): #return a copy of the grid
    Copy_Grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    for i in range(4):
        for j in range (4):
            Copy_Grid[i][j] = grid[i][j]  
    return Copy_Grid       

def grid_equal (grid1, grid2): #check if 2 grids are equal - return boolean value
    if grid1 == grid2:
        return True
    return False