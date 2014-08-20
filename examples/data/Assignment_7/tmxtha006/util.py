"""This program this program manipulates 2d arrays of size 4x4
Hebert Tema
28-04-2014"""


def border(grid):
    """puts a border around the grid"""
    l=len(grid)
    print("+", "-"*l*5, "+",sep="")
    for i in grid:
        print("|", end="")
        for j in i:
            if j==0: print("{0:5}".format(""),end="")
            else: print("{0:<5}".format(j),end="")
        print("|")
    print("+", "-"*l*5, "+",sep="")

#creates a 4x4 grid
def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
    return grid

#print out a grid
def print_grid(grid):
    border(grid)


def check_lost(grid):
    """checks if the game has been lost"""
    for i in range(4):
        for j in range(4):
            if not grid[i][j]: return False
            else: continue
    for i in range(3):
        for j in range(3):
            if grid[i][j]==grid[i][j+1] or grid[i][j]==grid[i+1][j]: return False
    return True
            

def check_won(grid):
    """checks if the game has been won"""
    for i in grid:
        for j in i:
            if j>=32:
                return True
    return False

def copy_grid(grid):
    """returns the copy of the original grid"""
    saved_grid=[[],[],[],[]]
    for i in range(4):
        for j in range(4):
            saved_grid[i].append(grid[i][j])
    return saved_grid

def grid_equal(grid1, grid2):
    """checks for equality between the two grids"""
    I=0
    for i in grid1:
        J=0
        for j in i:
            if j!=grid2[I][J]:
                return False
            else: J+=1
        I+=1
    return True