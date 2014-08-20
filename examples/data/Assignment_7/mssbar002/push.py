def push_up (grid):
    """merge grid values upwards"""
    # extract column 0 into 1-D Array
    temp = []
    for row in range(4):
        temp.append(grid[row][0])
    # push up in 1-D Array
    for n in range(3,0,-1):
        if temp[n]:
            if temp[n] == temp[n-1]:
                temp[n-1] = temp[n]*2
                temp[n] = 0
            elif temp[n-1] == 0:
                temp[n-1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for row in range(4):
        grid[row][0] = temp[row]
    
    # extract column 1 into 1-D Array
    temp = []
    for row in range(4):
        temp.append(grid[row][1])
    # push up in 1-D Array
    for n in range(3,0,-1):
        if temp[n]:
            if temp[n] == temp[n-1]:
                temp[n-1] = temp[n]*2
                temp[n] = 0
            elif temp[n-1] == 0:
                temp[n-1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for row in range(4):
        grid[row][1] = temp[row] 
        
    # extract column 2 into 1-D Array
    temp = []
    for row in range(4):
        temp.append(grid[row][2])
    # push up in 1-D Array
    for n in range(3,0,-1):
        if temp[n]:
            if temp[n] == temp[n-1]:
                temp[n-1] = temp[n]*2
                temp[n] = 0
            elif temp[n-1] == 0:
                temp[n-1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for row in range(4):
        grid[row][2] = temp[row] 
        
    # extract column 3 into 1-D Array
    temp = []
    for row in range(4):
        temp.append(grid[row][3])
    # push up in 1-D Array
    for n in range(3,0,-1):
        if temp[n]:
            if temp[n] == temp[n-1]:
                temp[n-1] = temp[n]*2
                temp[n] = 0
            elif temp[n-1] == 0:
                temp[n-1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for row in range(4):
        grid[row][3] = temp[row]        
    
def push_down (grid):
    """merge grid values downwards"""
    # extract column 0 into 1-D Array
    temp = []
    for row in range(4):
        temp.append(grid[row][0])
    # push up in 1-D Array
    for n in range(3):
        if temp[n]:
            if temp[n] == temp[n+1]:
                temp[n+1] = temp[n]*2
                temp[n] = 0
            elif temp[n+1] == 0:
                temp[n+1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for row in range(4):
        grid[row][0] = temp[row]

    # extract column 1 into 1-D Array
    temp = []
    for row in range(4):
        temp.append(grid[row][1])
    # push up in 1-D Array
    for n in range(3):
        if temp[n]:
            if temp[n] == temp[n+1]:
                temp[n+1] = temp[n]*2
                temp[n] = 0
            elif temp[n+1] == 0:
                temp[n+1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for row in range(4):
        grid[row][1] = temp[row]

    # extract column 2 into 1-D Array
    temp = []
    for row in range(4):
        temp.append(grid[row][2])
    # push up in 1-D Array
    for n in range(3):
        if temp[n]:
            if temp[n] == temp[n+1]:
                temp[n+1] = temp[n]*2
                temp[n] = 0
            elif temp[n+1] == 0:
                temp[n+1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for row in range(4):
        grid[row][2] = temp[row]
        
    # extract column 3 into 1-D Array
    temp = []
    for row in range(4):
        temp.append(grid[row][3])
    # push up in 1-D Array
    for n in range(3):
        if temp[n]:
            if temp[n] == temp[n+1]:
                temp[n+1] = temp[n]*2
                temp[n] = 0
            elif temp[n+1] == 0:
                temp[n+1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for row in range(4):
        grid[row][3] = temp[row]

def push_left (grid):
    """merge grid values left"""
    # extract row 0 into 1-D Array
    temp = []
    for column in range(4):
        temp.append(grid[0][column])
    # push up in 1-D Array
    for n in range(3,0,-1):
        if temp[n]:
            if temp[n] == temp[n-1]:
                temp[n-1] = temp[n]*2
                temp[n] = 0
            elif temp[n-1] == 0:
                temp[n-1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for column in range(4):
        grid[0][column] = temp[column]
        
    # extract row 1 into 1-D Array
    temp = []
    for column in range(4):
        temp.append(grid[1][column])
    # push up in 1-D Array
    for n in range(3,0,-1):
        if temp[n]:
            if temp[n] == temp[n-1]:
                temp[n-1] = temp[n]*2
                temp[n] = 0
            elif temp[n-1] == 0:
                temp[n-1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for column in range(4):
        grid[1][column] = temp[column]
        
    # extract row 2 into 1-D Array
    temp = []
    for column in range(4):
        temp.append(grid[2][column])
    # push up in 1-D Array
    for n in range(3,0,-1):
        if temp[n]:
            if temp[n] == temp[n-1]:
                temp[n-1] = temp[n]*2
                temp[n] = 0
            elif temp[n-1] == 0:
                temp[n-1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for column in range(4):
        grid[2][column] = temp[column]
        
    # extract row 3 into 1-D Array
    temp = []
    for column in range(4):
        temp.append(grid[3][column])
    # push up in 1-D Array
    for n in range(3,0,-1):
        if temp[n]:
            if temp[n] == temp[n-1]:
                temp[n-1] = temp[n]*2
                temp[n] = 0
            elif temp[n-1] == 0:
                temp[n-1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for column in range(4):
        grid[3][column] = temp[column]
    
def push_right (grid):
    """merge grid values right"""    
    # extract row 0 into 1-D Array
    temp = []
    for column in range(4):
        temp.append(grid[0][column])
    # push up in 1-D Array
    for n in range(3):
        if temp[n]:
            if temp[n] == temp[n+1]:
                temp[n+1] = temp[n]*2
                temp[n] = 0
            elif temp[n+1] == 0:
                temp[n+1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for column in range(4):
        grid[0][column] = temp[column]
        
    # extract row 1 into 1-D Array
    temp = []
    for column in range(4):
        temp.append(grid[1][column])
    # push up in 1-D Array
    for n in range(3):
        if temp[n]:
            if temp[n] == temp[n+1]:
                temp[n+1] = temp[n]*2
                temp[n] = 0
            elif temp[n+1] == 0:
                temp[n+1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for column in range(4):
        grid[1][column] = temp[column]
        
    # extract row 2 into 1-D Array
    temp = []
    for column in range(4):
        temp.append(grid[2][column])
    # push up in 1-D Array
    for n in range(3):
        if temp[n]:
            if temp[n] == temp[n+1]:
                temp[n+1] = temp[n]*2
                temp[n] = 0
            elif temp[n+1] == 0:
                temp[n+1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for column in range(4):
        grid[2][column] = temp[column]
        
    # extract row 3 into 1-D Array
    temp = []
    for column in range(4):
        temp.append(grid[3][column])
    # push up in 1-D Array
    for n in range(3):
        if temp[n]:
            if temp[n] == temp[n+1]:
                temp[n+1] = temp[n]*2
                temp[n] = 0
            elif temp[n+1] == 0:
                temp[n+1] = temp[n]
                temp[n] = 0
    # apply result to grid for colum 0
    for column in range(4):
        grid[3][column] = temp[column]