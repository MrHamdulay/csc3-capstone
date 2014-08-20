"""Manipulating 2-D Arrays
Keshin Vittee
30 April 2014"""

def create_grid(grid):
    height = 4
    for i in range(height):
        grid.append([0]*height)
        
#Need help formatting this
def print_grid(grid):
    print("+--------------------+")
    for row in range(4):
        print("|",end="")
        for col in range(4):
            if grid[row][col] == 0:
                print("{0:<5}".format(""),end='')
            else:
                print("{0:<5}".format(grid[row][col]), end="")
        print("|")
    print("+--------------------+")
        
def check_lost(grid):
    for r in range(4):
        for c in range(4):
            if 0 in grid:
                return False
            elif c == 3:
                if grid[r][c] == grid[r][c-1]:
                    return False
            elif grid[r][c]== grid[r][c-1] or grid[r][c] == grid[r][c+1]:
                return False
    return True

def check_won(grid):
    for r in range(4):
        for c in range(4):
            if grid[r][c] >= 32:
                return True
    return False
            
def copy_grid(grid):
    import copy
    copy_gr = copy.deepcopy(grid)
    return copy_gr
    
def grid_equal(grid1,grid2):
    if grid1 == grid2:
        return True
    else:
        return False
        


            
    
