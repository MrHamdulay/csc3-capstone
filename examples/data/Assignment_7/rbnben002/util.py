def create_grid(grid):
    for i in range(4):
        grid.append([" "]*4)
    return grid
def print_grid (grid):
    print("+--------------------+")
    for i in range(4):
        print('|',end='')
        for j in range(4):
            if grid[i][j]==0:
                print("{:5}".format(' '),sep='',end='')
            else:
                print('{:<5}'.format(grid[i][j]),sep='',end='')
        print('|')
    print("+--------------------+")
def check_lost (grid):
    if not 0 in grid:
        for i in range(3):
            for j in range(3):
                    if grid[i][j]==grid[i+1][j] or grid[i][j]==grid[i][j+1]:
                        return False
        return True
    else:
        return False
def check_won (grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j]>=32:
                return True           
    return False
def copy_grid (grid):
    gridtwo=[]
    gridtwo=make_grid(grida)
    for i in range(4):
        for j in range(4):
            gridrwo[i][j]=grid[i][j]
    return gridtwo
def grid_equal (grid1, grid2):
    for i in range(4):
        for j in range(4):
            if not grid1[i][j] == grid2[i][j]:
                return False
    return True