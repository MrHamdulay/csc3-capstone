'''Q2 of Assignment 7: Utility functions to manipulate 2-dimensional arrays of size 4x4
Patrick Boroughs
27 April 2014'''


def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    
    #make copy of origional grid
    printgrid=copy_grid(grid)
    
    #convert zeros to spaces
    for i in range(len(printgrid)):
        for j in range(len(printgrid)):
            if printgrid[i][j]==0:
                printgrid[i][j]=' '
     
    #format for printing grid in columns of 5
    gridForm="|{0:<5}{1:<5}{2:<5}{3:<5}|\n|{4:<5}{5:<5}{6:<5}{7:<5}|\n|{8:<5}{9:<5}{10:<5}{11:<5}|\n|{12:<5}{13:<5}{14:<5}{15:<5}|"
    
    #printing
    print("+--------------------+")
    
    print(gridForm.format(printgrid[0][0],printgrid[0][1],printgrid[0][2],printgrid[0][3],printgrid[1][0],printgrid[1][1],printgrid[1][2],printgrid[1][3],printgrid[2][0],printgrid[2][1],printgrid[2][2],printgrid[2][3],printgrid[3][0],printgrid[3][1],printgrid[3][2],printgrid[3][3])) 

    print("+--------------------+")

def check_lost (grid): 
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    
    #test if any zeros
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==0:
                return False
            
    #test if values in adjacent rows
    for i in range(len(grid)-1):
        for j in range(len(grid)):
            if grid[i][j]==grid[i+1][j]:
                return False
    
    #test if values in adjacent columns    
    for i in range(len(grid)):
        for j in range(len(grid)-1):
            if grid[i][j]==grid[i][j+1]:
                return False
    
    #lost        
    return True
                
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            
            if grid[i][j]>=32:
                return True
            
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    #create new grid
    copy=create_grid([])
    
    #append origional values into copy
    for i in range(len(copy)):
        for j in range(len(copy)):
            copy[i][j]=grid[i][j]
   
    return copy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        for j in range(4):
            #test if ever not equal
            if grid1[i][j]!=grid2[i][j]:
                return False
    return True
