#Azhar Aboobaker
#ABBAZH001
#30/04/2014

def create_grid(grid):
    for i in range(4):
        grid.append([0]*4) 
    return grid

def print_grid(grid):
    print("+", "-"*20, "+", sep="")
    for i in range(4):
        if i==0:
            print("|", sep="", end="")
        if grid[0][i]!=0:
            print("{:<5}".format(grid[0][i]), end="")
        else:
            print("{:<5}".format(""), end="")
        if i==3:
            print("|", sep="", end="")        
    print()
    for i in range(4):
        if i==0:
            print("|", sep="", end="")
        if grid[1][i]!=0:
            print("{:<5}".format(grid[1][i]), end="")
        else:
            print("{:<5}".format(" "), end="")
        if i==3:
            print("|", sep="", end="")
    print()
    for i in range(4):
        if i==0:
            print("|", sep="", end="")
        if grid[2][i]!=0:
            print("{:<5}".format(grid[2][i]), end="")
        else:
            print("{:<5}".format(" "), end="")
        if i==3:
            print("|", sep="", end="")        
    print()
    for i in range(4):
        if i==0:
            print("|", sep="", end="")
        if grid[3][i]!=0:
            print("{:<5}".format(grid[3][i]), end="")
        else:
            print("{:<5}".format(" "), end="")
        if i==3:
            print("|", sep="", end="")        
    print()
    print("+", "-"*20, "+", sep="")
    
def check_lost(grid):
    if grid[0].count(0)!=0 and grid[1].count(0)!=0 and grid[2].count(0)!=0 and grid[3].count(0)!=0:
        return False
    for row in range(3):                                                                                
        for column in range(3):
            if grid[row][column]==grid[row+1][column] or grid[row][column]==grid[row][column+1]:
                return False
    else:
        return True


def check_won(grid):
    for i in grid:
        for j in i:
            if j>=32:
                return True
    else:
        return False

def copy_grid(grid):
    gridcopy=[]
    for x in grid:
        gridcopy.append(list(x))
    return gridcopy

def grid_equal(grid1, grid2):
    if grid1==grid2:
        return True
    else:
        return False