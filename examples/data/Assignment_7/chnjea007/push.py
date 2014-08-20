# assignment 7 question 3
def push_up (grid):
    """merge grid values upwards"""
    for col in range(4):
        deleteDeadSpaceUp(col, grid)
        mergeUp(col, grid)
        deleteDeadSpaceUp(col, grid)
    

def push_down (grid):
    """merge grid values downwards"""  
    for col in range(4):
        deleteDeadSpaceDown(col, grid)
        mergeDown(col, grid)
        deleteDeadSpaceDown(col, grid)    

def push_left (grid):
    """merge grid values left"""
    for row in range(4):
        deleteDeadSpaceLeft(row, grid)
        mergeLeft(row, grid)
        deleteDeadSpaceLeft(row, grid)     

def push_right (grid):
    """merge grid values right""" 
    for row in range(4):
        deleteDeadSpaceRight(row, grid)
        mergeRight(row, grid)
        deleteDeadSpaceRight(row, grid)   

def deleteDeadSpaceUp(col, grid):
    for row in range(1, 4): 
        num = grid[row][col]
        if num != 0:
            for row2 in range(0, row):
                num2 = grid[row2][col]
                if num2 == 0:
                    grid[row][col], grid[row2][col] = 0, num
                    break    
                
def mergeUp(col, grid):
    for row in range (3):
        num = grid[row][col]
        num2 = grid[row+1][col]
        if num == num2:
            grid[row][col], grid[row+1][col] = num*2, 0


def deleteDeadSpaceDown(col, grid):
    for row in range(2, -1, -1): 
        num = grid[row][col]
        if num != 0:
            for row2 in range(3, row, -1):
                num2 = grid[row2][col]
                if num2 == 0:
                    grid[row][col], grid[row2][col] = 0, num
                    break    
                
def mergeDown(col, grid):
    for row in range (3, 0, -1):
        num = grid[row][col]
        num2 = grid[row-1][col]
        if num == num2:
            grid[row][col], grid[row-1][col] = num*2, 0


def deleteDeadSpaceLeft(row, grid):
    for col in range(1, 4): 
        num = grid[row][col]
        if num != 0:
            for col2 in range(0, col):
                num2 = grid[row][col2]
                if num2 == 0:
                    grid[row][col], grid[row][col2] = 0, num
                    break    
                
def mergeLeft(row, grid):
    for col in range (3):
        num = grid[row][col]
        num2 = grid[row][col+1]
        if num == num2:
            grid[row][col], grid[row][col+1] = num*2, 0


def deleteDeadSpaceRight(row, grid):
    for col in range(2, -1, -1): 
        num = grid[row][col]
        if num != 0:
            for col2 in range(3, col, -1):
                num2 = grid[row][col2]
                if num2 == 0:
                    grid[row][col], grid[row][col2] = 0, num
                    break    
                
def mergeRight(row, grid):
    for col in range (3, 0, -1):
        num = grid[row][col]
        num2 = grid[row][col-1]
        if num == num2:
            grid[row][col], grid[row][col-1] = num*2, 0