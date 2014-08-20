# Grid functions
# Lwazi Shezi
# 1 May 2014

# create a grid
def create_grid(grid):
    #grid = [['0']*4]*4 --- why won't this solution work?
    while len(grid) <=3:
        grid.append(['0']*4)
    return grid

# check if grids are equal
def grid_equal (grid1, grid2):
    if grid1 == grid2:
        return True
    else: return False
    
# check if a player has won or not
def check_won (grid):
    won = False
    for i in grid:
        for j in i:
            # if there is a value in the grid greater than 32, the player has won
            if int(j) >= 32:
                won = True
    return won
  
# make a copy of a grid  
def copy_grid(grid):
    import copy
    copy = copy.deepcopy(grid)
    return copy

# print a grid with a frame of dashes
def print_grid (grid):
    print('+'+'-'*20+'+')
    for i in grid:
        print('|',end = '')
        for j in i:
            if int(j) == 0:
                j = ''
            print('{0:<5}'.format(j),end = '')
        print('|')
    print('+'+'-'*20+'+')
    
# check if a player has won
def check_lost (grid):
    lost = False
    for i in grid:
        for j in range(len(i)):
            # if in the grid there are no 0 values and there are no equal consecutive numbers, the player has lost
            if int(j) == 0:
                if i[0] != 0 and i[0] != i[1] :
                        lost = True
            elif int(i[j]) != 0 and int(i[j]) != int(i[j-1]):
                lost = True
                    
            else: lost = False
    return lost

