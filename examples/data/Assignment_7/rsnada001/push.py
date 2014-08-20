"""question 1 assignment 7
2048 game function program
Adam Rosendorff
02 May 2014"""
row = []
def remove_spaces(row):
    for h in range(1,4):#for each position in row/column
        for k in range(1,h+1):#checking all prior positions to see if it can be moved
            if row[h-k] == 0:
                row[h-k] = row[h-k+1]
                row[h-k+1] = 0

def merge(row):
    remove_spaces(row)
    for i in range(3):
        if row[i] == row[i+1]:
            row[i] += row[i+1]
            row[i+1] = 0
            remove_spaces(row)
    return row

def push_up (grid):
    """merge grid values upwards"""    
    for j in range(4):
        row = []
        for i in range(4):
            row.append(grid[i][j])
        row = merge(row)
        for i in range(4):
            grid[i][j] = row[i]
        
    
def push_down (grid):
    """merge grid values downwards"""
    for j in range(4):
        row = []
        for i in range(4):
            row.append(grid[3-i][j])
        row = merge(row)
        for i in range(4):
            grid[i][j] = row[3-i]

def push_left (grid):
    """merge grid values left"""
    for i in range(4):
        row = []
        for j in range(4):
            row.append(grid[i][j])
        row = merge(row)
        for j in range(4):
            grid[i][j] = row[j]
    
def push_right (grid):
    """merge grid values right"""
    for i in range(4):
        row = []
        for j in range(4):
            row.append(grid[i][3-j])
        row = merge(row)
        for j in range(4):
            grid[i][j] = row[3-j]
