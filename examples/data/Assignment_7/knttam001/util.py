def create_grid (grid):
    """create a 4x4 grid"""
    height = 4
    for i in range (height):
        grid.append(["0"]*4) 
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in grid:
        print('|',end="")
        for x in i:
            if x == 0:
                x = ""
            print("{0:<5}".format(x),end="")
        print('|')
    print("+--------------------+")
    
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    tester = 0
    for i in grid: # checking for 0
        for x in i:
            if x == ' ':
                return false
    for i in range(4):
        for x in range (4): 
            value = grid[i][x]
            toright = x + 1
            if 0 <= toright < 4: # checking to the right
                if value == grid[i][toright]:
                    return False
            toleft = x - 1
            if 0 <= toleft <= 4: # checking to the left
                if value == grid[i][toleft]:
                    return False
            up = i - 1
            if 0 <= up < 4: # checking up 
                if value == grid[up][x]:
                    return False
            down = i + 1
            if 0 <= down < 4: # checking down
                    if value == grid[down][x]:
                        return False
    return True                
                    
            

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    tester = 0
    for i in grid:
        for x in i:
            if x >= 32:
                tester +=1
    if tester == 0:
        return False
    elif tester != 0:
        return True

def copy_grid (grid):
    """return a copy of the grid"""
    copy_grid = []
    create_grid(copy_grid)
    for i in range (4):
        for x in range (4):
            copy_grid[i][x] = grid[i][x]
    return copy_grid
    
def grid_equal (grid1, grid2):
    """check if 2 grids are equal = return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False

if __name__ == '__main__':
    a = []
    create_grid(a)
    print_grid(a)