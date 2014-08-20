"""Functions that manipulate the grid when a particular letter is pressed
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
        grid = [[2,2,8,8],[8,8,8,8],[6,6,6,6],[2,2,2,2]]
        
    return grid

def push_up (grid):
    """merge grid values upwards"""
    
    for col in range(4):
        for row in range(3):
            if grid[row][col] == grid[row+1][col]:
                grid[row][col] = grid[row+1][col]*2
                grid[row+1][col] = 0
                return grid

def push_down (grid):
    """merge grid values downwards"""
    
    for col in range(4):
        for row in range(3):
            if grid[row][col] == grid[row+1][col]:
                grid[row+1][col] = grid[row][col]*2
                grid[row][col] = 0
                print (grid)   
    

def push_left (grid):
     """merge grid values left"""   
     for row in range(4):
         for col in range(3):
             if grid[row][col] == grid[row][col+1]:
                 grid[row][col] = grid[row][col]*2
                 grid[row][col+1] = 0   
                 print (grid)
     
    

def push_right (grid):
     """merge grid values right"""
     for row in range(4):
         for col in range(3):
             if grid[row][col] == grid[row][col+1]:
                 grid[row][col+1] = grid[row][col]*2
                 grid[row][col] = 0 
                 print(grid)
    