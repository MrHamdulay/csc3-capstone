""" Rivoningo Seweya 
27 April 2014"""
grid = [[64,32,32,2],[8,4,2,0],[4,2,0,0],[2,0,0,0]]
import copy
def create_grid (grid):
    #create a 4x4 grid
    #create a loop
    for list_values in range(4):
        grid.append([0]*4)
    return grid
def print_grid (grid):
    """prints 4x4 grid in a 5 width colomn"""
    create_grid (grid)
    print("+"+"----"*5+"+")
    for hori in range(4):
        print("|",end="")
        for verti in range(4):
            if grid[hori][verti]==0:
                grid[hori][verti]=""
                print("{0:<5}".format(grid[hori][verti]),end="")
            else:
                print("{0:<5}".format(grid[hori][verti]),end="")
        print("|",end="")
        print("")
    print("+"+"----"*5+"+")

def copy_grid (grid):
    #create_grid (grid)
    #create a new grid
    grid2=[]
    #copy grid into grid2
    for hori in range(4):
        for verti in range(4):
            grid2=copy.deepcopy(grid)
    return grid2
def check_lost (grid):
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False
    #create loops
    for row in range(4):
    # second loop
        for col in range (4):
            #a decision ladder to determine if a player has lost the game
            if grid[row][col]==0:
                return False
    if grid[0][0]==grid[0][1] or grid[0][0]==grid[1][0]:
        return False
    if grid[0][3]==grid[0][2] or grid[0][3]==grid[1][3]:
        return False
    if grid[3][0]==grid[2][0] or grid[3][0]==grid[3][1]:
        return False
    if grid[3][3]==grid[2][3] or grid[3][3]==grid[3][2]:
        return False
    if grid[0][1]==grid[0][2] or grid[0][1]==grid[1][1]:
        return False
    if grid[0][2]==grid[1][2]:
        return False
    if grid[1][1]==grid[2][1] or grid[1][1]==grid[1][2] or grid[1][1]==grid[1][0]:
        return False
    if grid[2][1]==grid[2][0] or grid[2][1]==grid[2][2] or grid[2][1]==grid[3][1]:
        return False
    if grid[1][0]==grid[2][0]:
        return False
    if grid[1][2]==grid[1][3] or grid[1][2]==grid[2][2]:
        return False
    if grid[2][2]==grid[2][3] or grid[2][2]==grid[3][2]:
        return False
    if grid[3][1]==grid[3][2]:
        return False
    else:
        return True
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    true=""
    for hori in range (4):
        for verti in range (4):
            if grid[hori][verti]==" ":
                grid[hori][verti]=0
            if grid[hori][verti]>=32:
                true += "True"
            else:
                true += ""
    if "True" in true:
        return True
    else:
        return False
def grid_equal (grid1,grid2):
    """check if 2 grids are equal - return boolean value"""
    statement =""
    for hori in range (4):
        for verti in range (4):
            if grid2[hori][verti] != grid1[hori][verti]:
                statement += "False"
            else:
                statement += ""
    if "False" in statement:
        return False
    else:
        return True