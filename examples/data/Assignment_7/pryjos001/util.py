"""Module of utility functions to manipulate 2D arrays of size 4x4
Joseph Preyer
29 April 2014"""

def create_grid(grid):
    list1=grid
    for i in range(4):
        list1.append([0,0,0,0])
    return list1
        
def print_grid (grid):
    print("+"+20*"-"+"+")
    for i in range(4):
        print("|", end="")
        for j in range(4):
            if grid[i][j]==0:
                print (" ", end="")
            else:
                print(grid[i][j],end="")
            print((5-len(str(grid[i][j])))*" ",end="")
        print("|")
    print("+"+20*"-"+"+")
    
def check_lost(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                return False
            elif j>0:
                if grid[i][j]==grid[i][j-1]:
                    return False
            elif j<3:
                if grid[i][j]==grid[i][j+1]:
                    return False
    return True

def check_won (grid):
    for i in range(4):
            for j in range(4):
                if grid[i][j]>=32:
                    return True
    return False

def copy_grid (grid):
    import copy
    new_list=copy.deepcopy(grid)
    return new_list


def grid_equal (grid1,grid2):
    if grid1==grid2:
        return True
    else:
        return False

