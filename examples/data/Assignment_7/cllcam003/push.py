# program that combines values 
# Cameron Collum
# 29 April 2014

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
    for i in range(4):
        deleteDeadSpaceLeft(i, grid)
        mergeLeft(i, grid)
        deleteDeadSpaceLeft(i, grid)     

def push_right (grid):
    """merge grid values right""" 
    for i in range(4):
        deleteDeadSpaceRight(i, grid)
        mergeRight(i, grid)
        deleteDeadSpaceRight(i, grid)   

def deleteDeadSpaceUp(col, grid):
    for i in range(1, 4): 
        num = grid[i][col]
        if num != 0:
            for i2 in range(0, i):
                num2 = grid[i2][col]
                if num2 == 0:
                    grid[i][col], grid[i2][col] = 0, num
                    break    
                
def mergeUp(col, grid):
    for i in range (3):
        num = grid[i][col]
        num2 = grid[i+1][col]
        if num == num2:
            grid[i][col], grid[i+1][col] = num*2, 0


def deleteDeadSpaceDown(col, grid):
    for i in range(2, -1, -1): 
        num = grid[i][col]
        if num != 0:
            for i2 in range(3, i, -1):
                num2 = grid[i2][col]
                if num2 == 0:
                    grid[i][col], grid[i2][col] = 0, num
                    break    
                
def mergeDown(col, grid):
    for i in range (3, 0, -1):
        num = grid[i][col]
        num2 = grid[i-1][col]
        if num == num2:
            grid[i][col], grid[i-1][col] = num*2, 0


def deleteDeadSpaceLeft(i, grid):
    for col in range(1, 4): 
        num = grid[i][col]
        if num != 0:
            for col2 in range(0, col):
                num2 = grid[i][col2]
                if num2 == 0:
                    grid[i][col], grid[i][col2] = 0, num
                    break    
                
def mergeLeft(i, grid):
    for col in range (3):
        num = grid[i][col]
        num2 = grid[i][col+1]
        if num == num2:
            grid[i][col], grid[i][col+1] = num*2, 0


def deleteDeadSpaceRight(i, grid):
    for col in range(2, -1, -1): 
        num = grid[i][col]
        if num != 0:
            for col2 in range(3, col, -1):
                num2 = grid[i][col2]
                if num2 == 0:
                    grid[i][col], grid[i][col2] = 0, num
                    break    
                
def mergeRight(i, grid):
    for col in range (3, 0, -1):
        num = grid[i][col]
        num2 = grid[i][col-1]
        if num == num2:
            grid[i][col], grid[i][col-1] = num*2, 0
    
    
            
    
                
            