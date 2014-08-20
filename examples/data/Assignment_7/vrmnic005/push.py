#VRMNIC005
# assignment 7, question 3

def push_up(grid):
    """merge grid values upwards"""
    for col in range(4):
        changes = True
        while changes:
            changes = False
            for row in range(3):
                if grid[row][col] == 0 and grid[row+1][col] != 0:
                    grid[row][col] = grid[row+1][col]
                    grid[row+1][col] = 0
                    changes = True
                
        for row in range(3):
            if grid[row][col] == grid[row+1][col]:
                grid[row][col] *= 2
                grid[row+1][col] = 0

        changes = True
        while changes:
            changes = False
            for row in range(3):
                if grid[row][col] == 0 and grid[row+1][col] != 0:
                    grid[row][col] = grid[row+1][col]
                    grid[row+1][col] = 0
                    changes = True

def push_down(grid):
    """merge grid values downwards"""
    for col in range(4):
        changes = True
        while changes:
            changes = False
            for row in range(3, 0, -1):
                if grid[row][col] == 0 and grid[row-1][col] != 0:
                    grid[row][col] = grid[row-1][col]
                    grid[row-1][col] = 0
                    changes = True
                
        for row in range(3, 0, -1):
            if grid[row][col] == grid[row-1][col]:
                grid[row][col] *= 2
                grid[row-1][col] = 0

        changes = True
        while changes:
            changes = False
            for row in range(3, 0, -1):
                if grid[row][col] == 0 and grid[row-1][col] != 0:
                    grid[row][col] = grid[row-1][col]
                    grid[row-1][col] = 0
                    changes = True

def push_left(grid):
    """merge grid values left"""
    for row in range(4):
        changes = True
        while changes:
            changes = False
            for col in range(3):
                if grid[row][col] == 0 and grid[row][col+1] != 0:
                    grid[row][col] = grid[row][col+1]
                    grid[row][col+1] = 0
                    changes = True
                
        for col in range(3):
            if grid[row][col] == grid[row][col+1]:
                grid[row][col] *= 2
                grid[row][col+1] = 0

        changes = True
        while changes:
            changes = False
            for col in range(3):
                if grid[row][col] == 0 and grid[row][col+1] != 0:
                    grid[row][col] = grid[row][col+1]
                    grid[row][col+1] = 0
                    changes = True

def push_right(grid):
    """merge grid values right"""
    for row in range(4):
        changes = True
        while changes:
            changes = False
            for col in range(3, 0, -1):
                if grid[row][col] == 0 and grid[row][col-1] != 0:
                    grid[row][col] = grid[row][col-1]
                    grid[row][col-1] = 0
                    changes = True
                
        for col in range(3, 0, -1):
            if grid[row][col] == grid[row][col-1]:
                grid[row][col] *= 2
                grid[row][col-1] = 0

        changes = True
        while changes:
            changes = False
            for col in range(3, 0, -1):
                if grid[row][col] == 0 and grid[row][col-1] != 0:
                    grid[row][col] = grid[row][col-1]
                    grid[row][col-1] = 0
                    changes = True
