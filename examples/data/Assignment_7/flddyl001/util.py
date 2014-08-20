def create_grid (grid):
    """create a 4x4 grid"""

    height = 4
    
    for i in range(height):
        grid.append([0]*height)
       
    return grid


def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""    
    print("+--------------------+")    
    for row in range(4):
        row_str = ""
        for column in range(4):
            x = str(grid[row][column])
            if x == "0":
                x = " "
                row_str += x + " "*(5-len(x))
            else:
                row_str += x + " "*(5-len(x))
            
        print("|",row_str,"|",sep="")
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""

    for row in range(4):
        for column in range(4):
            
            x = grid[row][column]
            
            if x == 0:
                return False
            
            if row != 0 and row != 3: 
                if x == grid[row-1][column] or x == grid[row+1][column]:
                    return False
            elif row == 0:
                if x == grid[row+1][column]:
                    return False
            elif row == 3:
                if x == grid[row-1][column]:
                    return False                
                
            
            if column != 0 and column != 3:
                if x == grid[row][column-1] or x == grid[row][column+1]:
                    return False
            elif row == 0:
                if x == grid[row][column-1]:
                    return False
            elif row == 3:
                if x == grid[row][column+1]:
                    return False
            else:
            
                return True
            

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    winning = False
    for row in range(4):
        for column in range(4):
            if grid[row][column] >= 32:
                winning = True
    
    if winning == True:
        return True
    else:
        return False


def copy_grid (grid):
    """return a copy of the grid"""

    grid2 = []
    
    for row in range(4):
        inner = []
        for column in range(4):
            
            inner.append(grid[row][column])
        grid2.append(inner)
    
    #print(grid)    
    #print(grid2)
    return grid2

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    
    for row in range(4):
        for column in range(4):
            if grid1[row][column] != grid2[row][column]:
                return False
    return True