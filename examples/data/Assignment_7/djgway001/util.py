def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(0,4):
        grid.append("0"*4)

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+","-"*20,"+",sep="") #roof of box with corners
    for y in range(0,4):
        print("|",end="") #left wall
        for x in range(0,4):
            cell=grid[y][x]
            if cell==0:
                cell=" " #replace "0" with empty space
            print("{0:<{1}}".format(cell,5),end="") #print each inner list, alligned 5 left
        print("|") #right wall
    print("+","-"*20,"+",sep="") #floor of box with corners

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for y in range(0,4):
        for x in range(0,4):
            if grid[y][x]==0: #checks for 0's in the grid
                return False
            else: continue
    for y in range(3):
        for x in range(4):
            if grid[y][x]==grid[y+1][x]:
                return False
            else:
                continue #searches for verticle duplicates
    for y in range(4):
        for x in range(3):
            if grid[y][x]==grid[y][x+1]:
                return False
            else:
                continue
        return True #searches for horizontal duplicates

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for y in range(0,4):
        for x in range(0,4):
            if grid[y][x]>=32:
                return True
            else:
                continue
    return False #if tile 32 is found, game won

import copy
def copy_grid (grid):
    """return a copy of the grid"""
    return copy.deepcopy(grid) #copies grid, saves it under different "varible"

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for y in range(0,4):
        for x in range(0,4):
            if grid1[y][x]==grid2[y][x]:
                continue
            else:
                return False #compares each index of 2 different grids
    return True