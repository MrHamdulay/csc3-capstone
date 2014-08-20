#Thembekile Dubazana
#dbzphi002
#Assignment7:Q2

"""Module of 2D Arrays and functions"""

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    return grid

def  print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range(len(grid)):
        print("|",end="")
        for j in range(len(grid)):
            if grid[i][j]==0:
                print(grid[i][j]*""," "*5,end="",sep="")
            else:
                space=5-len(str(grid[i][j]))
                print(grid[i][j]," "*space,end="",sep="")
        print("|")
    print("+--------------------+")
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==0:
                return False
            else:
                if j != 3:
                    if grid[i][j]==grid[i][j+1]:
                        return False
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] >=32:
                    return True
    return False

def copy_grid (grid):#need help
    """return a copy of the grid"""
    copy=[]
    for i in range(4):
            copy.append([0]*4)
    for j in range(len(grid)):
        for k in range(len(grid)):
            copy[j][k]=grid[j][k]
    return copy
            

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True
            

