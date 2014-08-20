#Assignment 7
#Question 2
#Kiuran Naidoo
#27 April 2014

def create_grid(grid): #Creating a grid
    for rows in range(4):
        grid.append([0,0,0,0])
    return grid

def print_grid(grid):#Print A Grid

    print("+--------------------+")

    for rows in range(4):
        print("|", end="")
        for columns in range(4):
            if grid[rows][columns] == 0:
                print ("     ", end = "")
            else:
                print("{0:<5}".format(grid[rows][columns]), end = "")
        print("|")
    print("+--------------------+")
        
def check_lost(grid):
    
    for rows in range(4):
        if 0 in grid[rows]: #Check if there are 0's in grid
            return False
        for columns in range(3): #Check Adjacent cells for the same value
            if grid[rows][columns] == grid[rows][columns+1]:
                return False
    for rows in range(3):
        for columns in range(4):
            if grid[rows][columns] == grid[rows+1][columns]:
                return False

    return True
      
            
def check_won(grid):

    for rows in range(4): #Check if there is a value more than 32 in the grid
        for columns in range(4):
            if grid[rows][columns] >=32:
                return True
    return False

def copy_grid(grid):

    Grid2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    for rows in range(4):
        for columns in range (4):
            Grid2[rows][columns] = grid[rows][columns]  
    return Grid2      

    
   
            
def grid_equal (grid1, grid2): #Check if grids are equal
    if grid1 == grid2:
        return True
    else:
        return False
