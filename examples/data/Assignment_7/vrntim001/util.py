"""utiliy functions
Tim Mostert
27.4.14"""

def create_grid(grid):
    
    for i in range(4):
        grid.append([0]*4)
    return grid    

def print_grid(grid):
    print("+--------------------+")
    for row in range(4):
        print("|",end='')
        for col in range(4):
            n = grid[row][col]
            if n == 0:
                n = " "
            n_1 = "{0:<5}".format(str(n))
            print(n_1,end="")
        print("|",end='')    
        print()    
    print("+--------------------+")     
    
def check_lost(grid):
    
    for row in grid:
        previous = ""
        for position in row:
            if position == 0:
                return False
            if position == previous:
                return False
            previous = position
            
    a0last = ""
    a1last = ""
    a2last = ""
    a3last = ""
    
    for a in grid:
        if a[0] == a0last:
            return False
        if a[1] == a1last:
            return False
        if a[2] == a2last:
            return False
        if a[3] == a3last:
            return False
        a0last = a[0]
        a1last = a[1]
        a2last = a[2]
        a3last = a[3]
        
    return True 


def check_won(grid):
    for row in grid:
        for position in row:
            if position >= 32:
                return True
    return False

def copy_grid(grid):
    import copy
    new_grid = copy.deepcopy(grid)
    return new_grid

def grid_equal(grid1,grid2):
    if grid1 == grid2:
        return True
    return False
        
        
    