"""Mokoena Mafologele
02/05/2014
"""
#CREATE 4*4 grid
def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
def print_grid (grid):
    #print grid in square format
    print("+","-"*20,"+",sep="")
    for row in range(4):
        print("|",end="")
        for col in range(4):
            if grid[row][col]!=0:
                print("{0:<5}".format(grid[row][col]),end="")
            else:
                print("{0:<5}".format(""),end="")
        print("|")
    print("+","-"*20,"+",sep="")
def check_lost (grid):
    flag=True
    #Boolean operator manipulation
    for row in range(4):
            for col in range(4):
                if grid[row][col]==0:
                    flag=False
                    break
                else:
                    continue
    for row in range(1,3,1):
        for col in range(1,3,1):
            if grid[row][col]==grid[row-1][col] or grid[row+1][col]==grid[row][col] or grid[row][col]==grid[row][col-1] or grid[row][col]==grid[row][col+1]:
                flag=False
                break
    return flag
def check_won (grid):
    for row in range(4):
            for col in range(4):
                if grid[row][col]>=32:
                    return True
    return False           
def copy_grid (grid):
    #copy grid
    gridCopy=[[0 for x in range(4)] for x in range(4)]
    for i in range(4):
        for j in range(4):
            gridCopy[i][j]=grid[i][j]
    return gridCopy
def grid_equal (grid1, grid2):
    
    for row in range(4):
                for col in range(4):
                    if grid1[row][col]!=grid2[row][col]:
                        return False
    return True
    
