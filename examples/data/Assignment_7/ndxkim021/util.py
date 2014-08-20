#ashton

import copy

def create_grid(block):
    """create a 4x4 grid"""
    for i in range (4):
        block.append([0,0,0,0]) 
    
def print_grid (block):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range(len(block)):
        print("|", end = "")
        for j in range(len(block)):
            if (block[i][j] == 0):
                block[i][j] = "" 
            print ("{0: <5}".format(block[i][j]), end = "")
            if (block[i][j] == ""):
                block[i][j] = 0            
        print("|", end = "")
        print()
    print("+--------------------+")
    
def check_lost (block):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    lost = True
    for i in range(4):
        for j in range(3):
            if block[i][j] == block[i][j+1]: 
                lost = False

    for i in range(3):
        for j in range(4):
            if block[i][j] == block[i+1][j]: 
                lost = False    
              
    for i in range(4):
        for j in range(4):
            if block[i][j] == 0: 
                lost = False
            
    return lost
    
def check_won (block):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won = False
    for i in range(len(block)):
        for j in range(len(block)):
            if block[i][j] >= 32: 
                won = True
    return won    


def copy_grid(block):
    """return a copy of the grid"""
    return copy.deepcopy(block) 
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2: 
        return True
    else:
        return False