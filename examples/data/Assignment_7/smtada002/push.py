'''Assignment 7 question 3 push module
Adam Smith
27 April 2014'''


def push_up (grid): #merge grid values upwards
                
    for i in range (3):
        for j in range (3):
            for k in range (4):
                if grid[j][k] == 0:
                    grid[j][k], grid[j + 1][k] = grid[j + 1][k], 0    
    
    for i in range (3):
        for j in range (4):
            if grid[i][j] == grid[i + 1][j] and grid[i][j] != 0:
                grid[i][j], grid[i + 1][j] = grid[i][j]*2, 0
                    
    for i in range (3):
        for j in range (3):
            for k in range (4):
                if grid[j][k] == 0:
                    grid[j][k], grid[j + 1][k] = grid[j + 1][k], 0
    

def push_down (grid): #merge grid values downwards
    
    for i in range (3):
        for j in range (3, 0, -1):
            for k in range (4):
                if grid[j][k] == 0:
                    grid[j][k], grid[j -1][k] = grid[j -1][k], 0      
    
    for i in range (3, 0, -1):
        for j in range (4):
            if grid[i][j] == grid[i - 1][j] and grid[i][j] != 0:
                grid[i][j], grid[i - 1][j] = grid[i][j]*2, 0
                        
    for i in range (3):
        for j in range (3, 0, -1):
            for k in range (4):
                if grid[j][k] == 0:
                    grid[j][k], grid[j -1][k] = grid[j -1][k], 0    

def push_left (grid): #merge grid values left
    
    for i in range (3):
        for j in range (3):
            for k in range (4):
                if grid[k][j] == 0:
                    grid[k][j], grid[k][j + 1] = grid[k][j + 1], 0
                    
    for i in range (3):
        for j in range (4):
            if grid[j][i] == grid[j][i + 1] and grid[j][i] != 0:
                grid[j][i], grid[j][i + 1] = grid[j][i]*2, 0    
    
    for i in range (3):
        for j in range (3):
            for k in range (4):
                if grid[k][j] == 0:
                    grid[k][j], grid[k][j + 1] = grid[k][j + 1], 0

def push_right (grid): #merge grid values right
    
    for i in range (3):
        for j in range (3, 0, -1):
            for k in range (4):
                if grid[k][j] == 0:
                    grid[k][j], grid[k][j -1] = grid[k][j -1], 0      
    
    for i in range (3, 0, -1):
        for j in range (4):
            if grid[j][i] == grid[j][i - 1] and grid[j][i] != 0:
                grid[j][i], grid[j][i - 1] = grid[j][i]*2, 0
                        
    for i in range (3):
        for j in range (3, 0, -1):
            for k in range (4):
                if grid[k][j] == 0:
                    grid[k][j], grid[k][j -1] = grid[k][j -1], 0    