''' Assignment 7 Question 2
Matshepo Malatji MLTMAT013
2 May 2014'''

import util

def push_up (grid):
    """merge grid values upwards"""
    counter = 1
    while counter < 4:
        for row in range(1,4,1):
            for col in range(4):
                if grid[row -1][col] == grid[row][col]:
                    grid[row-1][col] *= 2
                    grid[row][col] = 0    
                elif grid[row - 1][col] == 0:
                    grid[row - 1][col] = grid[row][col]
                    grid[row][col] = 0
        counter += 1  
    return grid

def push_down (grid):
    """merge grid values downwards"""
    counter = 1
    while counter < 4:
        for row in range(3):
            for col in range(4):
                if grid[row +1][col] == grid[row][col]:
                    grid[row+1][col] *= 2
                    grid[row][col] = 0
                elif grid[row +1][col] == 0:
                    grid[row +1][col] = grid[row][col]
                    grid[row][col] = 0
        counter += 1  
    return grid    

def push_left (grid):
    """merge grid values left"""
    counter = 1
    while counter < 4:
        for row in range(4):
            for col in range(1,4,1):
                if grid[row][col-1] == grid[row][col]:
                    grid[row][col-1] *= 2
                    grid[row][col] = 0
                elif grid[row][col-1] == 0:
                    grid[row][col-1] = grid[row][col]
                    grid[row][col] = 0
        counter += 1  
    return grid        

def push_right (grid):
     """merge grid values right"""  
     counter = 1
     while counter < 4:
         for row in range(4):
             for col in range(3):
                 if grid[row][col+1] == grid[row][col]:
                    grid[row][col+1] *= 2
                    grid[row][col] = 0
                 elif grid[row][col+1] == 0:
                    grid[row][col+1] = grid[row][col]
                    grid[row][col] = 0
         counter += 1  
     return grid          