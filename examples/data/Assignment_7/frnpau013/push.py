
def push_left_1d(grid):
    grid2 = []
    for i in grid:
        if i != 0:
            grid2.append(i)
    if len(grid2) > 1:
        for i in range(len(grid2) - 1):
            if grid2[i] == grid2[i+1]:
                grid2[i] = grid2[i] * 2
                grid2[i+1] = 0
    grid3 = []
    for i in grid2:
        if i != 0:
            grid3.append(i)
    while len(grid3) < 4:
        grid3.append(0)
    return grid3

    
        
def push_left(grid):
    """merge grid values left""" 
    for i in range(4):
        grid[i] = push_left_1d(grid[i])
    return grid


def push_right_1d(grid):
    """pushes right in 1d"""
    grid = grid[::-1]
    grid = push_left_1d(grid)
    grid = grid[::-1] 
    return grid

def push_right(grid):
    for i in range(4):
            grid[i] = push_right_1d(grid[i])
    return grid    

def push_up(grid):
    for x in range(4):
        col_list = []
        for i in range(4):
            col_list.append(grid[i][x])
        col_list = push_left_1d(col_list)
        for i in range(4):
            grid[i][x] = col_list[i]
    return grid

def flip_grid_vert(grid):
    temp_grid = []
    for i in range(4):
        temp_row = grid[i]
        temp_row = temp_row[::-1]
        temp_grid.append(temp_row)
    temp_grid = temp_grid[::-1]
    return temp_grid

def push_down(grid):
    grid = flip_grid_vert(grid)
    grid = push_up(grid)
    grid = flip_grid_vert(grid)
    return grid
