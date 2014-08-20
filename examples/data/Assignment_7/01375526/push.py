def push_vals (vals):
    r = 0
    while (r+1)<len(vals):
        if (vals[r]==vals[r+1]):
            vals[r]=vals[r]+vals[r+1]
            del vals[r+1]
        r += 1
    vals = vals + [0,0,0,0]
    return vals    

def push_up (grid):
    for c in range (0, 4):
        vals = []
        for r in range (0, 4):
            if grid[r][c] != 0:
                vals.append (grid[r][c])
        vals = push_vals (vals)
        for r in range (0, 4):
            grid[r][c] = vals[r]

def push_down (grid):
    for c in range (0, 4):
        vals = []
        for r in range (3, -1, -1):
            if grid[r][c] != 0:
                vals.append (grid[r][c])
        vals = push_vals (vals)
        for r in range (3, -1, -1):
            grid[r][c] = vals[3-r]

def push_left (grid):
    for r in range (0, 4):
        vals = []
        for c in range (0, 4):
            if grid[r][c] != 0:
                vals.append (grid[r][c])
        vals = push_vals (vals)
        for c in range (0, 4):
            grid[r][c] = vals[c]

def push_right (grid):
    for r in range (0, 4):
        vals = []
        for c in range (3, -1, -1):
            if grid[r][c] != 0:
                vals.append (grid[r][c])
        vals = push_vals (vals)
        for c in range (3, -1, -1):
            grid[r][c] = vals[3-c]
            