"""Tevin Chetty
1 May 2014
Program to store functions"""

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append([0,0,0,0])#creates 2-d grid
    return grid

def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    import copy
    height=4
    new_grid=copy.deepcopy(grid) #copy's the grid
    for row in range (height):
        for col in range (height):
            if new_grid[row][col]==0:
                new_grid[row][col]=" "#fills all zeroes with empty spaces
    print("+", "-"*20, "+", sep="")
    for counter in range(4):
        #formatting so that each point in the grid becomes 5 characters wide
        print("|", "{0:<5}{1:<5}{2:<5}{3:<5}".format(new_grid[counter][0],new_grid[counter][1],new_grid[counter][2],new_grid[counter][3]),"|", sep="")        
    print("+", "-"*20, "+", sep="")

def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    height=4
    for row in range (height):
        for col in range (height):
            if grid[row][col]==0: #if empty
                return False
    #checks if there are adjacent values that are equal
    if grid[0][0]==grid[0][1] or grid[0][0]==grid[1][0]:
        return False
    if grid[0][3]==grid[0][2] or grid[0][3]==grid[1][3]:
        return False
    if grid[3][0]==grid[2][0] or grid[3][0]==grid[3][1]:
        return False
    if grid[3][3]==grid[3][2] or grid[3][3]==grid[2][3]:
        return False
    if grid[0][1]==grid[0][2] or grid[0][1]==grid[1][1]:
        return False
    if grid[0][2]==grid[1][2]:
        return False
    if grid[1][0]==grid[1][1] or grid[1][0]==grid[2][0]:
        return False
    if grid[2][0]==grid[2][1]:
        return False
    if grid[3][1]==grid[2][1] or grid[3][1]==grid[3][2]:
        return False
    if grid[3][2]==grid[2][2]:
        return False
    if grid[2][3]==grid[2][2] or grid[2][3]==grid[1][3]:
        return False
    if grid[1][3]==grid[1][2]:
        return False
    if grid[1][1]==grid[1][2] or grid[1][1]==grid[2][1]:
        return False
    if grid[2][1]==grid[2][2]:
        return False
    if grid[1][2]==grid[2][2]:
        return False
    else:
        return True

def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won=False
    height=4
    #Iterate through every point and checks if any of them are 32
    for row in range (height):
        for col in range (height):
            if grid[row][col]>=32: 
                won=True
                break
    return won
def copy_grid(grid):
    """return a copy of the grid"""
    import copy
    new_grid=copy.deepcopy(grid) #function to copy a grid
    return new_grid

def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else:
        return False