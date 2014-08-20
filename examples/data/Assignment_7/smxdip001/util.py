""""Dipanjali Samoo
SMXDIP001
Assignment 7_Question 2"""


def create_grid(grid):
    """will create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)

def print_grid (grid):
    """will print out a 4x4 grid in 5-width columns within a box"""
    print ("+"+"-"*20+"+")
    for i in range(4):
        print ("|",end='')
        for s in range(4):
            if grid[i][s] == 0:
                print ("     ",end='')
            else:
                print (str(grid[i][s])+(" "*(5-len(str(grid[i][s])))),end='')
        print ("|")
    print ("+"+"-"*20+"+")
    
def check_lost (grid):
    """this will return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    same = 0
    zero = 0
    for i in range(3):
        for s in range(1,4):
            if grid[i][s] == grid[i][s-1] or grid[i][s] == grid[i+1][s]:
                same+=1
                break
   
    for i in range(4):
        if 0 in grid[i]:
            zero+=1
            break
    if same==0 and zero==0:
        return True
    else:
        return False
            
def check_won (grid):
    """this will return True if a value>=32 is found in the grid; otherwise False"""
    won = 0
    for i in range(4):
            for s in range(4):
                if grid[i][s] >= 32:
                    won +=1
                    break
    if won == 0:
        return False
    else:
        return True
                
def copy_grid (grid):
    """ this will return a copy of the grid"""

    copy = []
    for i in range(4):
        copy.append([0]*4)
    for i in range(4):
        for s in range(4):
            copy[i][s] = grid[i][s]
    return copy

def grid_equal (grid1, grid2):
    """tis will help check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False