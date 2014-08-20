#Gina Horscroft, Assignment 7
#Util
import copy

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        temp = []
        for j in range(4):
            temp.append(0)
        grid.append(temp)    
        
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range (len(grid)):
        print("|", end = '')
        for e in range (4):        
            for a in range (5):
                if (grid[i][e]== 0):
                    print(" ", end = '')
                else:
                    #prevents from printing out number more than once.
                    st1 = str(grid[i][e])
                    print(grid[i][e], " "*(4-len(st1)), end = '')
                    break
        print("|", end = '')
        print()
    print("+--------------------+")
            
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    ret = True
    for i in range(4):
        for j in range(4):
            val = grid[i][j]
            if (val == 0):
                ret = False
    #checks if value = value to right
    for a in range(4):
        for b in range(3):
            val = grid[a][b]
            if (val == grid[a][b+1]):
                ret = False
    #checks if value = value one down
    for a in range(3):
        for b in range(4):
            val = grid[a][b]
            if (val == grid[a+1][b]):
                ret = False   
                         
    return ret

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    ret = False
    for i in range(4):
        for j in range(4):
            val = grid[i][j]    
            if (val >= 32):
                ret = True    
    return ret

def copy_grid (grid):
    """return a copy of the grid"""
    temp = copy.deepcopy(grid)
    return temp
    

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    equa = True
    if (len(grid1) == len(grid2)):#checks lengths are equal to start (so doen't loop out of bounds)
        for i in range(len(grid1)):
            if (grid1[i] != grid2[i]):
                equa = False
    return equa        
    
