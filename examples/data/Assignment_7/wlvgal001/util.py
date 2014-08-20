#Utility program provides all necessary functions for question 2 and 3
#Galya Wolov
#1 May 2014


def create_grid(grid):
    """create a 4x4 grid"""
    
    height = 4
    for i in range (height):
        grid.append ([0] * 4)
   

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    #Prints the grid with the border 
    print("+--------------------+")
    for i in range(4):
        print("|",end='')
        for j in range(4):       
            if grid[i][j] ==0:
                
                print(" ",end=(5-len(str(grid[i][j])))*" ")
            else:
                print(grid[i][j],end=(5-len(str(grid[i][j])))*" ")
        print("|")
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    #checks to see when the adjacent values are equal or if there are zeroes by comparing to variables 
    zeroexists= -1
    adjacent=-1
    for y in range(4):
        for x in range(4):
            if grid[x][y] == 0:
                zeroexists= 0
                
    for y1 in range(3):
        for x1 in range(3):
            if grid[x1][y1] == grid[x1+1][y1]:
                adjacent=0
    for y2 in range(3):
        for x2 in range(3):
            if grid[x2][y2] == grid[x2][y2+1]:
                adjacent=0    
     
    if zeroexists==-1 and adjacent==-1:
        return True
     
    else:
        return False
     
                
#checks to see if you win by getting 32 or above this is done to end game
def check_won (grid):
    for y in range(4):
        for x in range(4):
            if grid[x][y] == 32 or grid[x][y] >32:
                return True
            else:
                continue
    return False
    """return True if a value>=32 is found in the grid; otherwise False"""

#transposes what is in one grid into the other
def copy_grid (grid):
    grid3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            grid3[i][j]= grid[i][j] 
    return grid3
"""return a copy of the grid"""

#checks to see if one grid is quela to another
def grid_equal (grid1, grid2):
    if grid1 == grid2:
        return True
    else:
        return False
    """check if 2 grids are equal - return boolean value"""
    