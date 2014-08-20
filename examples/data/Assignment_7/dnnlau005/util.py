"""utility functions for 2048 game
Lauren Denny
29 April 2014"""

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)

def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+"+"-"*20+"+")               #top border of box
    for row in range(4):
        print("|",end="")               #left border of box
        for col in range(4):
            if grid[row][col]==0:   
                print(" "*5, end="")    #print blank spaces in place of 0's
            else:
                print("{0:<5}".format(grid[row][col]),end="") #print each number in grid in a 5-width column
        print("|")                      #right border of box
    print("+"+"-"*20+"+")               #bottow border of box

def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in grid:
        if 0 in row:        #return False if a 0 is found in any row in the grid
            return False
    for row in range(4):
        for col in range(4):
            #return False if any of the first 3 numbers in row 3 are equal to the number immediately to their right
            if row==3:
                if col<3 and grid[row][col]==grid[row][col+1]: 
                    return False
            #return False if any of the first 3 numbers in column 3 are equal to the number immediately below them
            elif col==3:
                if row<3 and grid[row][col]==grid[row+1][col]:
                    return False
            #return false if any other number in the grid is equal to the number immediately to their right of below them
            elif row<3 and col<3: 
                if grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row+1][col]:
                    return False
    #else return True if their are no 0's and no adjacent values equal    
    return True         

def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                return True
    return False      

def copy_grid(grid):
    """return a copy of the grid"""
   #create new 4x4 grid
    new_grid=[]                 
    for i in range(4):
        new_grid.append([0]*4) 
    #populate new_grid with same values as grid
    for row in range(4):
        for col in range(4):
            new_grid[row][col]=grid[row][col]
    #return copied grid    
    return new_grid

def grid_equal (grid1,grid2):
    """check if 2 grids are equal - return boolean value"""
    return grid1==grid2
