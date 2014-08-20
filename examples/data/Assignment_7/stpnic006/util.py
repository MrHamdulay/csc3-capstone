"""Nicholas Stephenson
Program to create grid for use in 20148"""

def create_grid (grid):
    for i in range(4):
        grid.append([0]*4)

def print_grid (grid):
    print("+--------------------+")
    for row in [0,1,2,3]:
        print("|", end = "")
        for col in [0,1,2,3]:
            if grid[row][col] == 0:
                print("     ",end= "")
            else: print(str(grid[row][col]) + " "*(5-(len(str(grid[row][col])))), end= "")
        print("|")
    print("+--------------------+")
#The above code creates a 4x4 grid with 5-width columns within a box, as stated by question

def check_lost (grid):
    flag = True
    for row in [0,1,2,3]:
        for col in [0,1,2,3]:
            if grid[row][col] == 0: 
                flag = False
            if row != 3:
                if grid[row][col] == grid[row+1][col]:
                    flag = False
            if col !=3:
                if grid[row][col] == grid[row][col+1]:
                    flag = False
    return flag
#The above code returns True if there are no 0 alues and no adjacent values that are equal; otherwise False, as states by the question


def check_won (grid):
    flag = False
    for row in [0,1,2,3]:
        for col in [0,1,2,3]:
            if grid[row][col] >= 32:
                flag = True
    return flag
#The above code returns True if a value >=32 is found in the grid; otherwise false, as stated by the question


def copy_grid (grid):
    newgrid= [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for row in [0,1,2,3]:
        for col in [0,1,2,3]:
            newgrid[row][col] = grid[row][col]
    return newgrid
#Code returns a carbon copy of the grid

def grid_equal (grid1,grid2):
    if grid1 == grid2:
        return True
    else:    return False
#Code checks if calues are equal