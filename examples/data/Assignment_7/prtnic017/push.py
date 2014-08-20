# PRTNIC017
# 28 April 2014


def push_up(grid):
    """merge grid values upwards"""
    # Translate Grid
    rows = [[], [], [], []]
    for i in range(len(grid)):
        rows[i] = [grid[0][i], grid[1][i], grid[2][i], grid[3][i]]
    # Push Left
    push_left(rows)
    # Translate Back
    for i in range(len(rows)):
        grid[i] = [rows[0][i], rows[1][i], rows[2][i], rows[3][i]]


def push_down(grid):
    """merge grid values downwards"""
    #translate grid
    rows = [[], [], [], []]
    for i in range(len(grid)):
        rows[i] = [grid[3][i], grid[2][i], grid[1][i], grid[0][i]]
    #push left
    push_left(rows)
    # Translate Back
    for i in range(len(grid)):
        grid[i] = [rows[0][3-i], rows[1][3-i], rows[2][3-i], rows[3][3-i]]


def push_right(grid):
    #reverse grid
    for i in range(len(grid)):
        grid[i].reverse()  # = grid[i][::-1]
    #push left
    push_left(grid)
    #reverse again
    for i in range(len(grid)):
        grid[i].reverse()  # = grid[i][::-1]


def push_left(grid):
    """merge grid values left"""
    for line in range(len(grid)):
        # first remove zero's
        while 0 in grid[line]:
            grid[line].remove(0)
        # combine
        for c in range(len(grid[line]) - 1):
            if grid[line][c] == grid[line][c + 1]:
                grid[line][c] *= 2
                grid[line][c + 1] = 0
                grid[line].remove(0)
                grid[line].append(0)
        grid[line] += ([0] * (4 - len(grid[line])))