def create_grid(grid):
    for y in range(4):
        row = []
        for x in range(4):
            row.append(0)
        grid.append(row)

def print_grid(grid):
    print('+--------------------+')
    for y in grid: #loop for each row
        print('|',end='')
        for x in y: #loop for each column
            if not x == 0:
                print('{:<5}'.format(x),end='')
            else:
                print('     ',end='')
        print('|')
    print('+--------------------+')

def check_lost(grid):
    #n = dimension of grid
    #checks from (0,0) to (n-1,n-1)
    for y in range(len(grid)-1): 
        for x in range(len(grid[y])-1):
            if not grid[y][x]:
                return False
            if grid[y][x] == grid[y][x+1]:
                return False
            if grid[y][x] == grid[y+1][x]:
                return False
    #checks the bottom row to n-1
    for x in range(len(grid[-1])-1):
        if not grid[-1][x]:
            return False
        if grid[-1][x] == grid[-1][x+1]:
            return False
    #checks the far right column to n-1
    for y in range(len(grid)-1):
        if not grid[y][-1]:
            return False
        if grid[y][-1] == grid[y+1][-1]:
            return False
    #checks the bottom-right corner
    if not grid[-1][-1]:
        return False
    return True

def check_won(grid):
    for y in grid:
        for x in y:
            if x >= 32:
                return True
    return False

def copy_grid(grid):
    grid_copy = [[],[],[],[]]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid_copy[y].append(grid[y][x])
    return grid_copy

def grid_equal(grid1, grid2):
    #assuming the grids will always be of equal dimensions
    for y in range(len(grid1)):
        for x in range(len(grid1[0])):
            if not grid1[y][x] == grid2[y][x]:
                return False
    return True
