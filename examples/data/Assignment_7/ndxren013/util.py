import copy

def create_grid(grid) :
    """create a 4x4 grid"""

    for i in range(4):
        tmp = []
        for j in range(4):
            tmp.append(0)
        grid.append(tmp)

def print_grid(grid) :
    """print out a 4x4 grid in 5-width columns within a box"""
    
    print("+--------------------+")

    for i in range (4):
        print('|', end = '')
        for j in range (4) :

            if grid[i][j] == 0:

                print (" " + " "*(5-(len(str(grid[i][j])))), end = "")
            
            else :
                print (str(grid[i][j]) + " "*(5-(len(str(grid[i][j])))), end = "")
        print("|")
        
    print("+--------------------+")

def check_lost(grid) :
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""

    flag = True
    
    for i in range (4) :

        for j in range(4) :

            if grid[i][j] == 0 :

                flag = False

    if flag == True :

        for i in range (0,4,1) :

            for j in range (0,4,1) :
                if i < 3 and j < 3:
                    if grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i+1][j] :
                        flag = False
                if i == 3 and j == 3:
                    continue
                if i == 3:
                    if grid[i][j] == grid[i][j + 1]:
                        flag = False
                if j == 3:
                    if grid[i][j] == grid[i + 1][j]:
                        flag = False

    return flag


def check_won(grid) :
    """return True if a value >= 32 is found in the grid; otherwise False"""

    flag = False

    for i in range (4) :

        for j in range (4) :

            if grid[i][j] >= 32 :

                flag = True

    return flag


def copy_grid(grid) :
    """return a copy of the grid"""

    return copy.deepcopy(grid)


def grid_equal(grid1, grid2) :
    """check if 2 grids are equal - return boolean value"""
    
    if grid1 == grid2 :

        return True
    
    else:

        return False

            
