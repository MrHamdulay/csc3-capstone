"""util module 
shannon clacey
1 may 2014"""

def create_grid(grid): #returns the grid
    for i in range(4):
        grid.append([0]*4)
    return grid

def print_grid(grid): #print the grid itself
    print("+", "-"*20, "+", sep='')
    for row in range(4):
        
        print("|", end="")
        for colum in range (4):
            if grid [row][column] == 0:
                print(" "*5, sep="", end="") #this line print a space if the itme is a zero
            else:
                print(grid[row][column], " "*(5-len(str(grid[row][coloumn]))),sep="",end="") #this ensures that each item within the grid is printed with appropriate spacing
        print("|", end="")
    print("+", "-"*20, "+", sep="")

def check_won(grid): #checks if the user has won the game (i.e. it returns true if a value of greater than 32 is in the grid and false if not)
    sentinel = False
    for row in range(4):
        for column in range(4):
            if grid[row][column] >= 32:
                sentinel = True
                return sentinel
    return sentinel

def check_lost(grid): #this checks if the user has lost the game by checking if the two grids are equal
    sentinel = True
    for row in range(4): #checks if there are any zeroes present
        for column in range (4):
            if grid[row][column] == 0:
                sentinel = False
                return sentinel 
    for row in range (4): #this checks if any element is equal to the element to its right
        for column in range (3):
            if grid[row][column] == grid[row][column+1]:
                sentinel = False
                return sentinel
    for row in range (3): #this checks if any of the elements inthe grid are equal to the element which is directly below
        for column in range (4):
            if grid[row][column] ==grid[row+1][column]:
                sentinel = False
                return sentinel
        
def copy_grid(grid):
    copy_grid =[[0]*4,[0]*4,[0]*4,[0]*4]
    for row in range(4):
        for column in range (4):
            copy_grid[row][column]=grid[row][column]
    return copy_grid

def grid_equal(grid1, grid2):
    if grid1 == grid2:
        return True # this is responsible for returning true if the two grids are equal
    else:
        return False
                    
    