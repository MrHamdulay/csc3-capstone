#Jono Field
#push.py
#1 May 

def push_up (grid):   #merge grid values upwards
    for x in range(4):
        deleteDeadSpaceUp(x, grid)
        mergeUp(x, grid)
        deleteDeadSpaceUp(x, grid)
    

def push_down (grid):   #merge grid values downwards
    for x in range(4):
        deleteDeadSpaceDown(x, grid)
        mergeDown(x, grid)
        deleteDeadSpaceDown(x, grid)    


def push_left (grid):  #merge grid values left
    for y in range(4):
        deleteDeadSpaceLeft(y, grid)
        mergeLeft(y, grid)
        deleteDeadSpaceLeft(y, grid)     


def push_right (grid):   #merge grid values right
    for y in range(4):
        deleteDeadSpaceRight(y, grid)
        mergeRight(y, grid)
        deleteDeadSpaceRight(y, grid)   


def deleteDeadSpaceUp(x, grid):      #delete old cells
    for y in range(1, 4): 
        num = grid[y][x]
        if num != 0:
            for y2 in range(0, y):
                num2 = grid[y2][x]
                if num2 == 0:
                    grid[y][x], grid[y2][x] = 0, num
                    break    

                
def mergeUp(x, grid):
    for y in range (3):
        num = grid[y][x]
        num2 = grid[y+1][x]
        if num == num2:
            grid[y][x], grid[y+1][x] = num*2, 0



def deleteDeadSpaceDown(x, grid):
    for y in range(2, -1, -1): 
        num = grid[y][x]
        if num != 0:
            for y2 in range(3, y, -1):
                num2 = grid[y2][x]
                if num2 == 0:
                    grid[y][x], grid[y2][x] = 0, num
                    break    

                
def mergeDown(x, grid):
    for y in range (3, 0, -1):
        num = grid[y][x]
        num2 = grid[y-1][x]
        if num == num2:
            grid[y][x], grid[y-1][x] = num*2, 0



def deleteDeadSpaceLeft(y, grid):
    for x in range(1, 4): 
        num = grid[y][x]
        if num != 0:
            for x2 in range(0, x):
                num2 = grid[y][x2]
                if num2 == 0:
                    grid[y][x], grid[y][x2] = 0, num
                    break    
                

def mergeLeft(y, grid):
    for x in range (3):
        num = grid[y][x]
        num2 = grid[y][x+1]
        if num == num2:
            grid[y][x], grid[y][x+1] = num*2, 0


def deleteDeadSpaceRight(y, grid):
    for x in range(2, -1, -1): 
        num = grid[y][x]
        if num != 0:
            for x2 in range(3, x, -1):
                num2 = grid[y][x2]
                if num2 == 0:
                    grid[y][x], grid[y][x2] = 0, num
                    break    

                
def mergeRight(y, grid):
    for x in range (3, 0, -1):
        num = grid[y][x]
        num2 = grid[y][x-1]
        if num == num2:
            grid[y][x], grid[y][x-1] = num*2, 0