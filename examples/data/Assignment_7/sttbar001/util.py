""" list of function
barak setton
27/04/2014"""

def create_grid(grid):
    for i in range(4):
        grid.append([0,0,0,0])

def print_grid (grid):
    print("+--------------------+")
    for i in range(4):
        print("|", end="")
        for j in range(4):
            if grid[i][j] != 0:
                print(grid [i][j],end=(" "*(5-len(str(grid[i][j])))))   
            else:
                print(" ",end=(" "*(4)))  

        print("|")
        
    print("+--------------------+")
    

def check_lost (grid):
    info = 0
    for i in range(4):              # checking if all are zeros 
        for j in range(4):
            if grid[i][j] == 0:
                info = 1
    for i in range(3):              # ching if adjacent values are equal
        for j in range(3):
            if grid[i+1][j] == grid[i][j]:
                info =1
    if info ==1:
        return False
    else:
        return True

def check_won (grid):
    for i in range(4):
        for j in range(4):
            if int(grid[i][j])>=32:
                return True
    else:
        return False
    """return True if a value>=32 is found in the grid; otherwise False"""

def copy_grid (grid):
    grid1 = []
    for i in range(4):
        grid1.append([grid[i][0] ,grid[i][1] ,grid[i][2] ,grid[i][3] ])
    return grid1
    """return a copy of the grid"""

def grid_equal (grid1, grid2):
    b = True
    if grid1 != grid2:
        b= False
    return b
    """check if 2 grids are equal - return boolean value"""