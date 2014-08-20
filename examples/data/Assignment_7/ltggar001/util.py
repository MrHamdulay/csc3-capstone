


def create_grid(grid):
    for x in range(4):
        grid.append([0,0,0,0])
    return grid


def print_grid (grid):
    def print_row(a):
        for i in range(0,4):
            if grid[a][i] == 0:
                print("     ",end="")
            elif 0<grid[a][i]<10:
                print(grid[a][i],"    ",sep="",end="")
            elif 10<grid[a][i]<100:
                print(grid[a][i],"   ",sep="",end="")
            elif 100<grid[a][i]<1000:
                print(grid[a][i],"  ",sep="",end="")
            elif 1000<grid[a][i]<10000:
                print(grid[a][i]," ",sep="",end="")
    print("+--------------------+")
    print("|",end="")
    print_row(0)
    print("|")
    print("|",end="")
    print_row(1)
    print("|")
    print("|",end="")
    print_row(2)
    print("|")
    print("|",end="")
    print_row(3)
    print("|")
    print("+--------------------+")
    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    check=0
    for i in range(0,4):
        for o in range(0,4):
            if grid[i][o] == 0:
                check=1
    for y in range(0,3):
        for u in range(0,3):
            if grid[y][u] == grid[y][u+1]:
                check=1
            elif grid[y][u] == grid[y+1][u]:
                check=1
    if check == 0:
        return True
    else:
        return False

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    check=0
    for i in range(0,4):
        for p in range(0,4):
            if grid[i][p] >= 32:
                check = 1
    if check == 0:
        return False
    else:
        return True
            
            
def copy_grid (grid):
    """return a copy of the grid"""
    grid2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for q in range(4):
        for w in range(4):
            grid2[q][w]=grid[q][w]
    return grid2
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    check = 0
    for q in range(0,4):
        for w in range(0,4):
            if grid1[q][w] != grid2[q][w]:
                check+=1
    if check == 0:
        return True
    else:
        return False
