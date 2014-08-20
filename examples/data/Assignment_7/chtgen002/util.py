"""
util
Genevieve Bronwyn Chetty (CHTGEN002)
02/05/2014
"""

def create_grid (grid): #grid creation of size 4
    for i in range(4):
        grid.append([0,0,0,0]) #append list to grid
    return grid

def print_grid(grid): 
    print("+--------------------+") #top border
    for i in range(4):
        print("|",end="") #left border
        for j in range(4):
            if(grid[i][j] == 0):
                print("{:<5}".format(" "), end = "") #format space 5
            else:
                print("{:<5}".format(grid[i][j]), end = "")
        print("|", end = "") #right border   
        print()
    print("+--------------------+") #bottom border

def check_won (grid): 
    for i in range(4):
        for j in range(4):
            if(grid[i][j]>=32):
                return True
    return False #if player has not won

def check_lost(grid):
    for i in range(4):
        for j in range(4):
            if(grid[i][j] == 0):
                return False
            if(j<3 and grid[i][j] == grid[i][j+1]):
                return False
            if(i<3 and grid[i][j] == grid[i+1][j]):
                return False
    return True #if player has lost

def copy_grid(grid):
    copy=[['','','',''],['','','',''],['','','',''],['','','','']]
    for i in range(4):
        for j in range(4):
            copy[i][j] = grid[i][j]
    return copy

def grid_equal (grid1, grid2):
    if(grid1 == grid2):
        return True
    else:
        return False
            
            
    



                