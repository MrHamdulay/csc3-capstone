"""modules to manipulate grid
tafara mtutu
29 april 2014"""

def create_grid(grid):
    """create a 4x4 grid"""
    list = grid
    for i in range (4):
        list.append([0]*4)    
    return list
        
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    #box = create_grid([])
    output = "{position:<5}"
    print("+--------------------+")
    for i in range(4):
        for j in range(6):
            if j == 0 or j == 5:
                print("|", end = "")
            else:
                if grid[i][j-1] == 0:
                    print(output.format(position = " "), end = "" )
                else:
                    print(output.format(position = grid[i][j-1]), end = "" )
        print()
    print("+--------------------+")
            
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for d in range(4):
        for h in range(4):
            if grid[d][h] == 0:
                return False
    
    for i in range(1,4):
        for j in range(1,4):
            if (grid[i-1][j-1] == grid[i-1][j]) or (grid[i-1][j-1] == grid[i][j-1]): #first area to scrutinize, just in case
                return False
    return True
  
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    list2 = []
    for i in range(4):
        list2.append([grid[i][0], grid[i][1],grid[i][2],grid[i][3]])    
    return list2       

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
            for j in range(4):
                if grid1[i][j] != grid2[i][j]:
                    return False
    return True
                    
                            