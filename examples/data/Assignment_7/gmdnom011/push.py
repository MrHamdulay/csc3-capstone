# Module of functions to merge gride values
# Nomsa Gamedze
# 28 April 2014

import util

def push_up (grid):
    """merge grid values upwards"""
    for i in (3, 2, 1):
        for c in range(4):
            if not grid[i][c]:
                continue
            if grid[i-1][c]:
                if grid[i-1][c] == grid[i][c]:
                    grid[i-1][c] += grid[i][c]
                    grid[i][c] = 0
            else:
                continue
    return grid

def push_down (grid):
    """merge grid values downwards"""
    for i in range(3):
            for c in range(4):
                if not grid[i][c]:
                    continue
                if grid[i+1][c]:
                    if grid[i-1][c] == grid[i][c]:
                        grid[i+1][c] += grid[i][c]
                        grid[i][c] = 0
                else:
                    continue
    return grid
        
def push_left (grid):
    """merge grid values left"""
    for i in range(4):
        for c in (3, 2, 1):
            if not grid[i][c]:
                continue
        if grid[i][c-1]: 
            if grid[i][c] == grid[i][c-1]:
                grid[i][c-1] += grid[i][c]
                grid[i][c] = 0
            else:
                continue
    return grid            

def push_right (grid):
    """merge grid values right"""
    for i in range(4):
        for c in range(3):
            if not grid[i][c]:
                continue
        if grid[i][c+1]:
            if grid[i][c] == grid[i][c+1]:
                grid[i][c+1] += grid[i][c]
                grid[i][c] = 0
            else:
                continue
    return grid