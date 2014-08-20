def move_piece(grid, x, y, dx, dy, done):
    if grid[y][x] == 0:
        return done

    val = grid[y][x]
    grid[y][x] = 0
    for i in range(4):
        if y+dy > 3 or x+dx > 3 or y+dy < 0 or x+dx < 0:
            grid[y][x] = val
            return done
        if grid[y+dy][x+dx] == val:
            if done:
                grid[y][x] = val
                return True
            else:
                grid[y+dy][x+dx] = 2*val
                return True
        elif grid[y+dy][x+dx] > 0:
            grid[y][x] = val
            return done
        x += dx
        y += dy

def push_up (grid):
    """merge grid values upwards"""
    for x in range(4):
        done = False
        for y in range(4):
            done = move_piece(grid, x, y, 0, -1, done)

def push_down (grid):
    """merge grid values downwards"""
    for x in range(4):
        done = False
        for y in range(4):
            done = move_piece(grid, x, 3-y, 0, 1, done)

def push_left (grid):
    """merge grid values left"""
    for y in range(4):
        done = False
        for x in range(4):
            done = move_piece(grid, x, y, -1, 0, done)

def push_right (grid):
    """merge grid values right""" 
    for y in range(4):
        done = False
        for x in range(4):
            done = move_piece(grid, 3-x, y, 1, 0, done)
