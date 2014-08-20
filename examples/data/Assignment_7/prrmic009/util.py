"""functions for 2048.py game and for question 2 of assignment 7
Mick Perring
29 April 2014"""

def create_grid(grid):   # creates a grid
    for i in range(4):
        grid.append([0,0,0,0])
    return grid

def print_grid(grid):   # prints a 'grid box' using input list
    print_grid = ""
    
    print("+--------------------+")   # prints top of 'box'

    for i in range(len(grid)):
        for j in range(len(grid)):
            if j == 0:
                print_grid += "|"  # prints left side of 'box'
            if grid[i][j] > 0:
                print_grid += str(grid[i][j]) + (5 - len(str(grid[i][j])))*" "  # prints values in grid
            else: print_grid += "     "    # if values = 0, prints spaces as placeholders
            if j == 3:
                print_grid += "|"  # prints right side of 'box'
        print(print_grid)
        print_grid = ""
        
    print("+--------------------+")   # prints bottom of 'box'
    
def check_lost(grid):   # checks to see if player has lost the game
    lost = True
    for i in range(4):   # checks for zeros in grid
        for j in range(4):
            if grid[i][j] == 0:
                lost = False
                
    if lost == True:   # if no zeros, checks if equal adjacent values to merge
        for i in range(4):
            for j in range(3):
                if grid[i][j] == grid [i][j+1]:
                    lost = False
        for i in range(3):
            for j in range(4):
                if grid [i][j] == grid [i+1][j]:
                    lost = False
    return lost

def check_won(grid):   # checks to see if player has won the game
    won = False
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:  # if player gets 32, player wins
                won = True
    return won

def copy_grid(grid):   # makes a permanent copy of the input grid
    import copy
    grid2 = copy.deepcopy(grid)
    return grid2

def grid_equal(grid1, grid2):   # checks if two grids are equal
    for i in range(4):
        for j in range(4):
            if grid1[i][j]!=grid2[i][j]:
                return False
    return True