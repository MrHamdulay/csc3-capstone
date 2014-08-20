#Assignment 7.3
#Michael Gant
#27/04/2014

def push_up (grid):
    """merge grid values upwards"""
    for i in range(1,3+1):
        for j in range(4):
            if grid[i][j] != 0:
                currPos = i
                while grid[currPos-1][j] == 0 and currPos > 0:
                    grid[currPos-1][j] = grid[currPos][j]
                    grid[currPos][j] = 0
                    currPos = currPos - 1
    
    for i in range(3):
        for j in range(4):
            if grid[i][j] == grid[i+1][j]:
                grid[i][j] = 2*grid[i][j]
                for k in range(i+1,3):
                    grid[k][j] = grid[k+1][j]
                grid[3][j] = 0

def push_down (grid):
    """merge grid values downwards"""
    for i in range(2,0-1,-1):
        for j in range(4):
            if grid[i][j] != 0:
                currPos = i
                while currPos < 3 and grid[currPos+1][j] == 0:
                    grid[currPos+1][j] = grid[currPos][j]
                    grid[currPos][j] = 0
                    currPos = currPos + 1
    for i in range(3,1-1,-1):
        for j in range(4):
            if grid[i][j] == grid[i-1][j]:
                grid[i][j] = 2*grid[i][j]
                for k in range(i-1,0-1,-1):
                    grid[k][j] = grid[k-1][j]
                grid[0][j] = 0
                    


def push_left (grid):
    """merge grid values left"""
    for j in range(1,3+1):
        for i in range(4):
            if grid[i][j] != 0:
                currPos = j
                while currPos > 0 and grid[i][currPos-1] == 0:
                    grid[i][currPos-1] = grid[i][currPos]
                    grid[i][currPos] = 0
                    currPos = currPos - 1
    for j in range(3):
        for i in range(4):
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] = 2*grid[i][j]
                for k in range(j+1,3):
                    grid[i][k] = grid[i][k+1]
                grid[i][3] = 0
                

def push_right (grid):
    """merge grid values right"""
    for j in range(2,0-1,-1):
        for i in range(4):
            if grid[i][j] != 0:
                currPos = j
                while currPos < 3 and grid[i][currPos+1] == 0:
                    grid[i][currPos+1] = grid[i][currPos]
                    grid[i][currPos] = 0
                    currPos = currPos + 1
    for j in range(3,0,-1):
        for i in range(4):
            if grid[i][j] == grid[i][j-1]:
                grid[i][j] = 2* grid[i][j]
                for k in range(j-1,0,-1):
                    grid[i][k] = grid[i][k-1]
                grid[i][0] = 0
            