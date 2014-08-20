# Question 2 - Assignment 7
# Oliver Harrison
# 27 April 2014




def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([])
        for j in range(4):
            grid[i].append(0)
    return grid
    

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+", "-"*len(grid[0]*5), "+", sep="")
    for i in range(4):
        print("|", end="")
        for j in range(4):
            if grid[i][j] != 0:
                print('%-5s' % grid[i][j], end="")
            else:
                print(" "*5, end="")
        print("|")
    print("+", "-"*len(grid[0]*5), "+", sep="")
    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(3):
        for j in range(3):
            #for x in range(-1, 2, 2):
                #print(grid[i+x][j+x])
                #print(grid[i][j+x])
            if grid[i+1][j] != grid[i][j] and grid[i][j+1] != grid[i][j] and grid[i+1][j] != 0 and grid[i][j+1]:
                continue
            else:
                return False
    return True

                    
                

            
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True
            else:
                continue
    return False
            

def copy_grid (grid):
    """return a copy of the grid"""
    from copy import copy, deepcopy
    new__grid = deepcopy(grid)
    return new__grid
    """new_grid=[]
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[i][j])
    return new_grid"""

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False 
#print_grid([[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]])
#print(check_lost([[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]))