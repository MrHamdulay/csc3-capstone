"""push_up, push_down, push_left and push_right functions for 2048.py
Mick Perring
01 May 2014"""

def push_up(grid):  # merges all equal values up (including if space in between)
    for i in range(4):
        if grid[0][i] == grid[1][i]:
            grid[0][i] += grid[1][i]
            grid[1][i] = 0
        elif grid[1][i] == 0 and grid[0][i] == grid[2][i]:
            grid[0][i] += grid[2][i]
            grid[2][i] = 0
        elif grid[1][i] == 0 and grid[2][i] == 0 and grid[0][i] == grid[3][i]:
            grid[0][i] += grid[3][i]
            grid[3][i] = 0
        if grid[1][i] == grid[2][i]:
            grid[1][i] += grid[2][i]
            grid[2][i] = 0
        elif grid[2][i] == 0 and grid[1][i] == grid[3][i]:
            grid[1][i] += grid[3][i]
            grid[3][i] = 0
        if grid[2][i] == grid[3][i]:
            grid[2][i] += grid[3][i]
            grid[3][i] = 0
    for i in range(4):   # compresses all values up
        if grid[0][i] == 0 and grid[1][i] == 0 and grid[2][i] == 0 and grid[3][i] == 0:
            continue
        if grid[0][i] == 0:
            if grid[1][i] != 0:
                grid[0][i] = grid[1][i]
                grid[1][i] = 0
                if grid[2][i] != 0 and grid[3][i] == 0:
                    grid[1][i] = grid[2][i]
                    grid[2][i] = 0
                elif grid[2][i] != 0 and grid[3][i] != 0:
                    grid[1][i] = grid[2][i]
                    grid[2][i] = grid[3][i]
                    grid[3][i] = 0
                elif grid[2][i] == 0 and grid[3][i] != 0:
                    grid[1][i] = grid[3][i]
                    grid[3][i] = 0
            elif grid[1][i] == 0 and grid[2][i] != 0:
                grid[0][i] = grid[2][i]
                grid[2][i] = 0
                if grid[3][i] != 0:
                    grid[2][i] = grid[3][i]
                    grid[3][i] = 0
            elif grid[1][i] == 0 and grid[2][i] == 0 and grid[3][i] != 0:
                grid[0][i] = grid[3][i]
                grid[3][i] = 0
        if grid[1][i] == 0:
            if grid[2][i] != 0:
                grid[1][i] = grid[2][i]
                grid[2][i] = 0
                if grid[3][i] != 0:
                    grid[2][i] = grid[3][i]
                    grid[3][i] = 0
            elif grid[2][i] == 0 and grid[3][i] != 0:
                grid[1][i] = grid[3][i]
                grid[3][i] = 0
        if grid[2][i] == 0:
            grid[2][i] = grid[3][i]
            grid[3][i] = 0
            
def push_down(grid):  # merges all equal values down (including if space in between)
    for i in range(4):
        if grid[3][i] == grid[2][i]:
            grid[3][i] += grid[2][i]
            grid[2][i] = 0
        elif grid[2][i] == 0 and grid[3][i] == grid[1][i]:
            grid[3][i] += grid[1][i]
            grid[1][i] = 0
        elif grid[2][i] == 0 and grid[1][i] == 0 and grid[3][i] == grid[0][i]:
            grid[3][i] += grid[0][i]
            grid[0][i] = 0
        if grid[2][i] == grid[1][i]:
            grid[2][i] += grid[1][i]
            grid[1][i] = 0
        elif grid[1][i] == 0 and grid[2][i] == grid[0][i]:
            grid[2][i] += grid[0][i]
            grid[0][i] = 0
        if grid[1][i] == grid[0][i]:
            grid[1][i] += grid[0][i]
            grid[0][i] = 0
    for i in range(4):  # compresses all values down
        if grid[3][i] == 0 and grid[2][i] == 0 and grid[1][i] == 0 and grid[0][i] == 0:
            continue
        if grid[3][i] == 0:
            if grid[2][i] != 0:
                grid[3][i] = grid[2][i]
                grid[2][i] = 0
                if grid[3][i] != 0 and grid[2][i] == 0:
                    grid[2][i] = grid[1][i]
                    grid[1][i] = 0
                elif grid[1][i] != 0 and grid[0][i] != 0:
                    grid[2][i] = grid[1][i]
                    grid[1][i] = grid[0][i]
                    grid[0][i] = 0
                elif grid[1][i] == 0 and grid[0][i] != 0:
                    grid[2][i] = grid[0][i]
                    grid[0][i] = 0
            elif grid[2][i] == 0 and grid[1][i] != 0:
                grid[3][i] = grid[1][i]
                grid[1][i] = 0
                if grid[0][i] != 0:
                    grid[1][i] = grid[0][i]
                    grid[0][i] = 0
            elif grid[2][i] == 0 and grid[1][i] == 0 and grid[0][i] != 0:
                grid[3][i] = grid[0][i]
                grid[0][i] = 0
        if grid[2][i] == 0:
            if grid[1][i] != 0:
                grid[2][i] = grid[1][i]
                grid[1][i] = 0
                if grid[0][i] != 0:
                    grid[1][i] = grid[0][i]
                    grid[0][i] = 0
            elif grid[1][i] == 0 and grid[0][i] != 0:
                grid[2][i] = grid[0][i]
                grid[0][i] = 0
        if grid[1][i] == 0:
            grid[1][i] = grid[0][i]
            grid[0][i] = 0
            
def push_left(grid):  # merges all equal values to the left (including if space in between)
    for i in range(4):
        if grid[i][0] == grid[i][1]:
            grid[i][0] += grid[i][1]
            grid[i][1] = 0
        elif grid[i][1] == 0 and grid[i][0] == grid[i][2]:
            grid[i][0] += grid[i][2]
            grid[i][2] = 0
        elif grid[i][1] == 0 and grid[i][2] == 0 and grid[i][0] == grid[i][3]:
            grid[i][0] += grid[i][3]
            grid[i][3] = 0
        if grid[i][1] == grid[i][2]:
            grid[i][1] += grid[i][2]
            grid[i][2] = 0
        elif grid[i][2] == 0 and grid[i][1] == grid[i][3]:
            grid[i][1] += grid[i][3]
            grid[i][3] = 0
        if grid[i][2] == grid[i][3]:
            grid[i][2] += grid[i][3]
            grid[i][3] = 0
    for i in range(4):  # compresses all values to the left
        if grid[i][0] == 0 and grid[i][1] == 0 and grid[i][2] == 0 and grid[i][3] == 0:
            continue
        if grid[i][0] == 0:
            if grid[i][1] != 0:
                grid[i][0] = grid[i][1]
                grid[i][1] = 0
                if grid[i][2] != 0 and grid[i][3] == 0:
                    grid[i][1] = grid[i][2]
                    grid[i][2] = 0
                elif grid[i][2] != 0 and grid[i][3] != 0:
                    grid[i][1] = grid[i][2]
                    grid[i][2] = grid[i][3]
                    grid[i][3] = 0
                elif grid[i][2] == 0 and grid[i][3] != 0:
                    grid[i][1] = grid[i][3]
                    grid[3][i] = 0
            elif grid[i][1] == 0 and grid[i][2] != 0:
                grid[i][0] = grid[i][2]
                grid[i][2] = 0
                if grid[i][3] != 0:
                    grid[i][2] = grid[i][3]
                    grid[i][3] = 0
            elif grid[i][1] == 0 and grid[i][2] == 0 and grid[i][3] != 0:
                grid[i][0] = grid[i][3]
                grid[i][3] = 0
        if grid[i][1] == 0:
            if grid[i][2] != 0:
                grid[i][1] = grid[i][2]
                grid[i][2] = 0
                if grid[i][3] != 0:
                    grid[i][2] = grid[i][3]
                    grid[i][3] = 0
            elif grid[i][2] == 0 and grid[i][3] != 0:
                grid[i][1] = grid[i][3]
                grid[i][3] = 0
        if grid[i][2] == 0:
            grid[i][2] = grid[i][3]
            grid[i][3] = 0
            
def push_right(grid):
    for i in range(4): # merges all equal values to the right (including if space in between) 
        if grid[i][3] == grid[i][2]:
            grid[i][3] += grid[i][2]
            grid[i][2] = 0
        elif grid[i][2] == 0 and grid[i][3] == grid[i][1]:
            grid[i][3] += grid[i][1]
            grid[i][1] = 0
        elif grid[i][2] == 0 and grid[i][1] == 0 and grid[i][3] == grid[i][0]:
            grid[i][3] += grid[i][0]
            grid[i][0] = 0
        if grid[i][2] == grid[i][1]:
            grid[i][2] += grid[i][1]
            grid[i][1] = 0
        elif grid[i][1] == 0 and grid[i][2] == grid[i][0]:
            grid[i][2] += grid[i][0]
            grid[i][0] = 0
        if grid[i][1] == grid[i][0]:
            grid[i][1] += grid[i][0]
            grid[i][0] = 0
    for i in range(4):    # compresses all values to the right
        if grid[i][3] == 0 and grid[i][2] == 0 and grid[i][1] == 0 and grid[i][0] == 0:
            continue
        if grid[i][3] == 0:
            if grid[i][2] != 0:
                grid[i][3] = grid[i][2]
                grid[i][2] = 0
                if grid[i][3] != 0 and grid[i][2] == 0:
                    grid[i][2] = grid[i][1]
                    grid[i][1] = 0
                elif grid[i][1] != 0 and grid[i][0] != 0:
                    grid[i][2] = grid[i][1]
                    grid[i][1] = grid[i][0]
                    grid[i][0] = 0
                elif grid[i][1] == 0 and grid[i][0] != 0:
                    grid[i][2] = grid[i][0]
                    grid[i][0] = 0
            elif grid[i][2] == 0 and grid[i][1] != 0:
                grid[i][3] = grid[i][1]
                grid[i][1] = 0
                if grid[i][0] != 0:
                    grid[i][1] = grid[i][0]
                    grid[i][0] = 0
            elif grid[i][2] == 0 and grid[i][1] == 0 and grid[i][0] != 0:
                grid[i][3] = grid[i][0]
                grid[i][0] = 0
        if grid[i][2] == 0:
            if grid[i][1] != 0:
                grid[i][2] = grid[i][1]
                grid[i][1] = 0
                if grid[i][0] != 0:
                    grid[i][1] = grid[i][0]
                    grid[i][0] = 0
            elif grid[i][1] == 0 and grid[i][0] != 0:
                grid[i][2] = grid[i][0]
                grid[i][0] = 0
        if grid[i][1] == 0:
            grid[i][1] = grid[i][0]
            grid[i][0] = 0