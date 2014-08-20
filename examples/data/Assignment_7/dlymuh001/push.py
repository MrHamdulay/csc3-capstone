ROWS = 4
COLS = 4

def popzeros (values, index):
    size = len(values)
    new_values = [0]*size
    new_i = 0
    for i in range(0,size):
        if values[i] != 0:
            new_values[new_i] = values[i]
            new_i += 1
    return new_values[index]

def push_list (values, index):
    '''push list values towards index 0'''
    size = len(values)
    nonzerovals = [0]*size
    for i in range(0,size):
        nonzerovals[i] = popzeros(values,i)
    new_values = [0]*size
    new_i = 0 #index for new_values
    i = 0
    while i < size-1:
        if nonzerovals[i] == 0:
            break
        elif nonzerovals[i] == nonzerovals[i+1]:
            new_values[new_i] = 2*nonzerovals[i]
            nonzerovals[i+1] = 0
            new_i += 1
            i += 2
        else:
            new_values[new_i] = nonzerovals[i]
            new_i += 1
            i += 1
    if nonzerovals[size-1] != 0: new_values[new_i] = nonzerovals[size-1]
    return new_values[index]

def push_up (grid):
    """merge grid values upwards"""
    values = [0]*ROWS
    for col in range(0,COLS):
        for row in range(0,ROWS):
            values[row] = grid[row][col]
        for row in range(0,COLS):
            grid[row][col] = push_list(values,row)
    return grid

def push_down (grid):
    """merge grid values downwards"""
    values = [0]*ROWS
    for col in range(0,COLS):
        for row in range(0,ROWS):
            values[row] = grid[ROWS-row-1][col]
        for row in range(0,COLS):
            grid[row][col] = push_list(values,ROWS-row-1)
    return grid   

def push_left (grid):
    """merge grid values left"""
    values = [0]*COLS
    for row in range(0,ROWS):
        for col in range(0,COLS):
            values[col] = grid[row][col]
        for col in range(0,COLS):
            grid[row][col] = push_list(values,col)
    return grid
            
def push_right (grid):
    """merge grid values right"""
    values = [0]*ROWS
    for row in range(0,ROWS):
        for col in range(0,COLS):
            values[col] = grid[row][COLS-col-1]
        for col in range(0,COLS):
            grid[row][col] = push_list(values,COLS-col-1)
    return grid
