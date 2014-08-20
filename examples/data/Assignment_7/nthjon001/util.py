"""Utility functions to manipulate 2D arrays
Jonathan Nathan
27 April 2014"""

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])
    return grid
        
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for y in range (4):
        print ("|", sep = '', end = '')
        for x in range (4):
            if grid[y][x] != 0:
                print(grid[y][x], ' ' * (5-len(str((grid[y][x])))), sep = '', end = '') 
            else:
                print('     ', end = '')
        print("|", sep = '')
    print("+--------------------+")
    
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    game_over = ''
    for i in grid:
        if 0 in i:
            game_over += 'no'
        

    if  grid[0][0] == grid[0][1] or grid[0][0] == grid[1][0]:
        game_over += 'no'
    if  grid[0][1] == grid[0][2] or grid[0][1] == grid[1][1]:
        game_over += 'no'
    if  grid[0][2] == grid[0][3] or grid[0][2] == grid[1][2]:
        game_over += 'no'
    if  grid[0][3] == grid[1][3]:
        game_over += 'no'
        
    if  grid[1][0] == grid[1][1] or grid[1][0] == grid[2][0]:
        game_over += 'no'
    if  grid[1][1] == grid[1][2] or grid[1][1] == grid[2][1]:
        game_over += 'no'
    if  grid[1][2] == grid[1][3] or grid[1][2] == grid[2][2]:
        game_over += 'no'
    if  grid[1][3] == grid[2][3]:
        game_over += 'no'
    
    if  grid[2][0] == grid[2][1] or  grid[2][0] == grid[3][0]:
        game_over += 'no'
    if  grid[2][1] == grid[2][2] or  grid[2][1] == grid[3][1]:
        game_over += 'no'
    if  grid[2][2] == grid[2][3] or  grid[2][2] == grid[3][2]:
        game_over += 'no'
    if  grid[2][3] == grid[3][3]:
        game_over += 'no'
        
    if  grid[3][0] == grid[3][1]:
        game_over += 'no'
    if  grid[3][2] == grid[3][3]:
        game_over += 'no'
     # game_over variable will contain at least one 'no' if a move is still possible
    if game_over.find('no') != -1:
        return False
    else: return True
    



def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    check = 0
    for i in grid:
        for r in i:
            if r >= 32:
                check = 1
                
    if check == 1:
        return True
    else: return False
    
def copy_grid(grid):
    """return a copy of the grid"""
    import copy 
    return copy.deepcopy(grid)
            
    
def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else: return False

