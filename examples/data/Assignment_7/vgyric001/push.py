
# assignment 7 
# question 3
# richard van gysen
#30 April 2014


def push_up (grid):

    """merge grid values upwards"""

    for i in range(4):
        deleteDeadSpaceUp(i, grid)
        mergeUp(i, grid)
        deleteDeadSpaceUp(i, grid)

def push_down (grid):

    """merge grid values downwards"""  

    for i in range(4):
        deleteDeadSpaceDown(i, grid)
        mergeDown(i, grid)
        deleteDeadSpaceDown(i, grid)    

def push_left (grid):

    """merge grid values left"""

    for j in range(4):
        deleteDeadSpaceLeft(j, grid)
        mergeLeft(j, grid)
        deleteDeadSpaceLeft(j, grid)     

def push_right (grid):

    """merge grid values right""" 

    for j in range(4):
        deleteDeadSpaceRight(j, grid)
        mergeRight(j, grid)
        deleteDeadSpaceRight(j, grid)   


def deleteDeadSpaceUp(i, grid):

    for j in range(1, 4): 
        num = grid[j][i]
        if num != 0:
            for j2 in range(0, j):
                num2 = grid[j2][i]
                if num2 == 0:
                    grid[j][i], grid[j2][i] = 0, num

                    break    

def mergeUp(i, grid):

    for j in range (3):
        num = grid[j][i]
        num2 = grid[j+1][i]
        if num == num2:
            grid[j][i], grid[j+1][i] = num*2, 0


def deleteDeadSpaceDown(i, grid):

    for j in range(2, -1, -1): 

        num = grid[j][i]
        if num != 0:
            for j2 in range(3, j, -1):
                num2 = grid[j2][i]
                if num2 == 0:
                    grid[j][i], grid[j2][i] = 0, num
                    break    

                

def mergeDown(i, grid):

    for j in range (3, 0, -1):
        num = grid[j][i]
        num2 = grid[j-1][i]
        if num == num2:
            grid[j][i], grid[j-1][i] = num*2, 0



def deleteDeadSpaceLeft(j, grid):

    for i in range(1, 4): 
        num = grid[j][i]
        if num != 0:
            for i2 in range(0, i):
                num2 = grid[j][i2]
                if num2 == 0:
                    grid[j][i], grid[j][i2] = 0, num
                    break    

                

def mergeLeft(j, grid):

    for i in range (3):
        num = grid[j][i]
        num2 = grid[j][i+1]
        if num == num2:
            grid[j][i], grid[j][i+1] = num*2, 0

def deleteDeadSpaceRight(j, grid):

    for i in range(2, -1, -1): 
        num = grid[j][i]
        if num != 0:
            for i2 in range(3, i, -1):
                num2 = grid[j][i2]
                if num2 == 0:
                    grid[j][i], grid[j][i2] = 0, num
                    break    

                

def mergeRight(j, grid):
    for i in range (3, 0, -1):
        num = grid[j][i]
        num2 = grid[j][i-1]
        if num == num2:
            grid[j][i], grid[j][i-1] = num*2, 0




