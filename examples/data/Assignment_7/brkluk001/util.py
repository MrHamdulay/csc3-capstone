'''Program to to manipulate 2-dimensional arrays of size 4x4
30 April 2013
Luke Barker'''

def create_grid(grid):
    for i in range(4):      
        grid.append([0]*4)    #prints a 2D grid of 5 spaces
    

def print_grid (grid):
    print('+--------------------+')
    for i in range(4):
        print('|', end="")
        for j in range(4):
            if grid[i][j]==0:
                position=" "     #changes 0 to spaces
            else: position = grid[i][j]
            position = "{0:<5}".format(position)   #format grid to sample I/O 
            print(position, end="")
        print('|')
    print('+--------------------+')
    

def check_lost (grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
    for i in range(4):
        for j in range(4):
            if i == 0 and j==0:
                if grid[i][j] == grid[i+1][j] or grid[i][j]== grid[i][j+1]:     #checks if there are the same number next to any number when the grid is full
                    return False
            if i == 0 and j==3:
                if grid[i][j] == grid[i][j-1] or grid[i][j]== grid[i+1][j]:     #checks if there are the same number next to any number when the grid is full
                    return False
            if i == 3 and j==3:
                if grid[i][j] == grid[i][j-1] or grid[i][j]== grid[i-1][j]:     #checks if there are the same number next to any number when the grid is full
                    return False
            if i == 3 and j==0:
                if grid[i][j] == grid[i-1][j] or grid[i][j]== grid[i][j+1]:     #checks if there are the same number next to any number when the grid is full
                    return False
            if (i == 0 and j == 1) or (i== 3 and j== 1):       #checks if there are the same number next to any number when the grid is full
                if grid[i][j] == grid[i][j+1]:
                    return False
            if (i == 1 and j == 0) or (i == 1 and j == 3):   #checks if there are the same number next to any number when the grid is full
                if grid[i][j] == grid[i+1][j]:
                    return False
            if (i == 1 and j == 1) or (i == 1 and j == 2) or (i == 2 and j == 1) or (i == 2 and j == 2):    #checks if there are the same number next to any number when the grid is full
                if grid[i][j] == grid[i-1][j] or grid[i][j]== grid[i][j+1] or grid[i][j] == grid[i][j-1] or grid[i][j]== grid[i+1][j]:
                    return False
    return True
            
                
    
                    
def check_won (grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:     #checks to see whether an number in the grid is greater or equal to 32
                return True
    return False

def copy_grid (grid):      
    new_grid = [[],[],[],[]]
    for i in range(4):
        for j in range(4):
            new_grid[i].append(grid[i][j])    #create a new grid to for continuation of the game
    return new_grid

def grid_equal (grid1, grid2):   
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:    #checks whether the old grid in equal to the new grid
                return False
    return True