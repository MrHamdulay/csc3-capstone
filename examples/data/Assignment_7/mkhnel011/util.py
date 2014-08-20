""" a module of utility functions on grids
nelisile mkhwebane
question 2 assignment 7
30/04/2014 """

""" a function that creates a grid of 4X4 """
height = 4
grid=[]
def create_grid(grid):
    global height
    for i in range (height):
        grid.append ([0]* 4)
        
    #for row in range (height):
        #for col in range (height):
            #grid[row][col] = row + col
grid=[]

""" a function that prints out the grid"""

def print_grid(grid):
    #rid = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
    global height
    print("+","-"*20,"+",sep="")
    for row in range (height):
        print("|",end="")
        for col in range (height):
            if grid[row][col] !=0:
                print ("{0:<5}".format(grid[row][col]), end="")
            else:
                print("     ",end="")
        print("|",end="")
        print ()
    print("+","-"*20,"+",sep="")

""" checking for 0 values, and if there aren't adjascent equal numbers
it should return True aren't any, and False if there are """
def check_lost (grid):
    #grid = [[4,2,8,2],[2,2,16,8],[16,32,8,4],[4,8,4,2]]
    global height
    for row in range (height):
        for col in range(height):
            if grid == [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]:
                return True
            if grid[row][col]!=0:
                return False
            elif grid[row][col] == grid[row][col+1]:
                return False
            elif grid[row][col] == grid [row+1][col]:
                return False
        else:
            return True
""" a program that checks if the player has won """

def check_won (grid):
    won = False
    #grid = [[4,2,8,2],[2,2,16,8],[16,32,8,4],[4,8,4,2]]
    global height
    for row in range (height):
        for col in range (height):
            if grid[row][col] >= 32:
                won = True
    if won:
        return True
    else:
        return False

""" a function that returns a copy of the grid """

def copy_grid (grid):
    import copy
   #grid = [[4,2,8,2],[2,2,16,8],[16,32,8,4],[4,8,4,2]]
    return copy.deepcopy(grid)

""" a function to check if two grids are equal """

def grid_equal (grid1,grid2):
    equal = True
    for row in range(height):
        for col in range(height):
            if grid1[row][col] != grid2[row][col]:
                equal = False
    if not equal:
        return False
    else:
        return True