""" Set of merging functions that merge adjacent equal values and eliminate gaps """
__author__ = 'Stephen Temple'
__date__ = '2014/04/29'


def push_up(grid):
    """ Merge grid values upwards """
    # First add
    for col in range(4):
        for row in range(4):
            if grid[row][col] != 0:
                for r in range(row + 1, 4):
                    if grid[r][col] != 0 and grid[row][col] != grid[r][col]:
                        break
                    elif grid[row][col] == grid[r][col]:
                        grid[row][col] *= 2
                        grid[r][col] = 0
                        break
    # Then push
    for col in range(4):
        for row in range(4):
            if grid[row][col] == 0:
                for r in range(row + 1, 4):
                    if grid[r][col] != 0:
                        grid[row][col] = grid[r][col]
                        grid[r][col] = 0
                        break
                else:
                    break


def push_down(grid):
    """ Merge grid values downwards """
    # First add
    for col in range(4):
        for row in range(3, -1, -1):
            if grid[row][col] != 0:
                for r in range(row - 1, -1, -1):
                    if grid[r][col] != 0 and grid[row][col] != grid[r][col]:
                        break
                    elif grid[row][col] == grid[r][col]:
                        grid[row][col] *= 2
                        grid[r][col] = 0
                        break
    # Then push
    for col in range(4):
        for row in range(3, -1, -1):
            if grid[row][col] == 0:
                for r in range(row - 1, -1, -1):
                    if grid[r][col] != 0:
                        grid[row][col] = grid[r][col]
                        grid[r][col] = 0
                        break
                else:
                    break


def push_left(grid):
    """ Merge grid values left """
    # First add
    for row in range(4):
        for col in range(4):
            if grid[row][col] != 0:
                for c in range(col + 1, 4):
                    if grid[row][c] != 0 and grid[row][col] != grid[row][c]:
                        break
                    elif grid[row][col] == grid[row][c]:
                        grid[row][col] *= 2
                        grid[row][c] = 0
                        break
    # Then push
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                for c in range(col + 1, 4):
                    if grid[row][c] != 0:
                        grid[row][col] = grid[row][c]
                        grid[row][c] = 0
                        break
                else:
                    break


def push_right(grid):
    """ Merge grid values right """
    # First add
    for row in range(4):
        for col in range(3, -1, -1):
            if grid[row][col] != 0:
                for c in range(col - 1, -1, -1):
                    if grid[row][c] != 0 and grid[row][col] != grid[row][c]:
                        break
                    elif grid[row][col] == grid[row][c]:
                        grid[row][col] *= 2
                        grid[row][c] = 0
                        break
    # Then push
    for row in range(4):
        for col in range(3, -1, -1):
            if grid[row][col] == 0:
                for c in range(col - 1, -1, -1):
                    if grid[row][c] != 0:
                        grid[row][col] = grid[row][c]
                        grid[row][c] = 0
                        break
                else:
                    break