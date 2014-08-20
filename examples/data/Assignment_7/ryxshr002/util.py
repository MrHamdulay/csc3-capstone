"""Shriya Roy
1 May 2014
program to manipulate grids"""


def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])
    return grid


def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    
    import copy
    grid2=copy.deepcopy(grid)#copying the grid
    for row in range(4):
        for col in range(4):
            if grid2[row][col]==0:
                grid2[row][col]=" "

                
    
    print("+--------------------+")
    print("|"+"{0:<5}{1:<5}{2:<5}{3:<5}".format(grid2[0][0],grid2[0][1],grid2[0][2],grid2[0][3])+"|")
    print("|"+"{0:<5}{1:<5}{2:<5}{3:<5}".format(grid2[1][0],grid2[1][1],grid2[1][2],grid2[1][3])+"|")
    print("|"+"{0:<5}{1:<5}{2:<5}{3:<5}".format(grid2[2][0],grid2[2][1],grid2[2][2],grid2[2][3])+"|")
    print("|"+"{0:<5}{1:<5}{2:<5}{3:<5}".format(grid2[3][0],grid2[3][1],grid2[3][2],grid2[3][3])+"|")
    
    print("+--------------------+")
    


def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range(4):
        for col in range(4):
            #conditions to be false
            if grid[row][col]==0:
                return False
    if grid[0][0]==grid[0][1] or grid[0][0]==grid[1][0]:
        return False
    if grid[3][0]==grid[2][0] or grid[3][0]==grid[3][1]:
        return False
    if grid[0][3]==grid[1][3] or grid[0][3]==grid[0][2]:
        return False
    if grid[3][3]==grid[3][2] or grid[3][3]==grid[2][3]:
        return False
    if grid[2][0]==grid[3][0] or grid[2][0]==grid[2][1] or grid[2][0]==grid[1][0]:
        return False
    if grid[1][0]==grid[1][1] or grid[1][0]==[0][0] or grid[1][0]==grid[2][0]:
        return False
    if grid[0][1]==grid[1][1] or grid [0][1]==grid[0][2] or grid[0][1]==[0][0]:
            return False
    if grid[0][2]==grid[1][2] or grid[0][2]==grid[0][3] or grid[0][2]==grid[0][1]:
            return False
    if grid[1][3]==grid[0][3] or grid[1][3]==grid[2][3] or grid[1][3]==grid[1][2]:
            return False
    if grid[2][3]==grid[1][3] or grid[2][3]==grid[2][2] or grid[2][3]==grid[3][3]:
            return False
    if grid[3][2]==grid[3][3] or grid[3][2]==grid[2][2] or grid[3][2]==grid[3][1]:
            return False
    if grid[3][1]==grid[3][2] or grid[3][1]==grid[2][1] or grid[3][1]==grid[3][0]:
            return False
    if grid[1][1]==grid[1][2] or grid[1][1]==grid[0][1] or grid[1][1]==grid[0][1] or grid[1][1]==grid[1][0]:
            return False
    if grid[1][2]==grid[1][3] or grid[1][2]==grid[0][2] or grid[1][2]==grid[0][2] or grid[1][2]==grid[1][1]:
            return False
    if grid[2][1]==grid[2][2] or grid[2][1]==grid[3][1] or grid[2][1]==grid[2][0] or grid[2][1]==grid[1][1]:
            return False
    if grid[2][2]==grid[2][3] or grid[2][2]==grid[1][2] or grid[2][2]==grid[2][1] or grid[2][2]==grid[3][2]:
            return False
    else:
        return True
                
                
    
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won=False#inital variable is false
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                won=True
                break
    return won                
            


def copy_grid(grid):
    """return a copy of the grid"""
    import copy
    grid3=copy.deepcopy(grid)
    return grid3
            

def grid_equal(grid1,grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else:
        return False 

    
    