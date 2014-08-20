# push.py
# a program to complete the code of the 2048 program
# using the utilitiy module from question 2
# Thomas Konigkramer
# 28 April 2014

"""see push_right (grid) for comments: that was done first"""

def push_up (grid):
    """merge grid values upwards"""

    for loopall in range(3): 
        for row in range(1,4):    
            for column in range(4): 
                if grid[row-1][column] == 0:
                    grid[row-1][column] = grid[row][column]
                    grid[row][column] = 0
                                
    for row in range(1,4):
        for column in range(4):                
            if grid[row-1][column] == grid[row][column]:
                grid[row-1][column] = 2 * grid[row][column]
                grid[row][column] = 0
                                
    for loopall in range(3): 
        for row in range(1,4):    
            for column in range(4): 
                if grid[row-1][column] == 0:
                    grid[row-1][column] = grid[row][column]
                    grid[row][column] = 0       
                                    
    return

def push_down (grid):
    """merge grid values downwards"""
    
    for loopall in range(3): 
        for row in range(2,-1,-1):    
            for column in range(4): 
                if grid[row+1][column] == 0:
                    grid[row+1][column] = grid[row][column]
                    grid[row][column] = 0
                            
    for row in range(2,-1,-1):
        for column in range(4):                
            if grid[row][column] == grid[row+1][column]:
                grid[row+1][column] = 2 * grid[row][column]
                grid[row][column] = 0
                            
    for loopall in range(3): 
        for row in range(2,-1,-1):    
            for column in range(4): 
                if grid[row+1][column] == 0:
                    grid[row+1][column] = grid[row][column]
                    grid[row][column] = 0       
    
    return    
    
def push_left (grid):
    """merge grid values left"""
    
    for loopall in range(3): 
        for row in range(4):    
            for column in range(3): 
                if grid[row][column] == 0:
                    grid[row][column] = grid[row][column+1]
                    grid[row][column+1] = 0
                                    
    for row in range(4):
        for column in range(3):                
            if grid[row][column] == grid[row][column+1]:
                grid[row][column] = 2 * grid[row][column+1]
                grid[row][column+1] = 0
    
    for loopall in range(3): 
        for row in range(4):    
            for column in range(3): 
                if grid[row][column] == 0:
                    grid[row][column] = grid[row][column+1]
                    grid[row][column+1] = 0       
                                        
    return    

def push_right (grid):
    """merge grid values right"""
    
    """shift grid to the right - i.e. eliminate all zeroes"""
    for loopall in range(3): # repeat process three times to shift
        for row in range(4):    
            for column in range(2,-1,-1): # so that can make from left to right: don't move 
                                          # third column, because already on far right
                if grid[row][column+1] == 0:
                    grid[row][column+1] = grid[row][column]
                    grid[row][column] = 0
    
    """adding adjecent pairs of numbers that are equal"""                
    for row in range(4):
        for column in range(2,-1,-1):                
                if grid[row][column] == grid[row][column+1]:
                    grid[row][column+1] = 2 * grid[row][column]
                    grid[row][column] = 0
                    
    """repetition of first step to shift right after gaps were opened from merging"""
    for loopall in range(3): 
            for row in range(4):    
                for column in range(2,-1,-1): 
                    if grid[row][column+1] == 0:
                        grid[row][column+1] = grid[row][column]
                        grid[row][column] = 0    
                    
    return