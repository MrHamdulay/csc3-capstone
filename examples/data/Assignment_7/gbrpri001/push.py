"""PRIYANKA GOBERDHAN
01/05/2014"""

"""Merge values upwards"""
def push_up (grid):
    for colm in range (len(grid)):
        temp = [0,0,0,0,0,0,0,0]
        for row in range(4):
            temp[row] = grid[row][colm]
        for i in range (4):
            if temp[i] == 0:
                if temp[i+1] == 0:
                    if temp[i+2] == 0:
                        if temp[i+3] == 0:
                            temp[i] = temp[i+3]
                            temp[i+3] = 0
                        else:
                            temp[i] = temp[i+3]
                            temp[i+3] = 0
                    else:
                        temp[i] = temp[i+2]
                        temp[i+2] = 0
                else:
                    temp[i] = temp[i+1]
                    temp[i+1] = 0
        for j in range (4):
            if temp[j] == temp[j+1]:
                temp[j] += temp[j+1]
                temp[j+1] = temp[j+2]
                temp[j+2] = temp[j+3]
                temp[j+3] = temp[j+4]
        for k in range (4):
            grid[k][colm] = temp[k]
            
"""Merge values downwards"""            
def push_down (grid):
    for colm in range (len(grid)):
        temp = [0,0,0,0,0,0,0,0]
        for row in range(4):
            temp[row] = grid[row][colm]
        for i in range (3,-1,-1):
            if temp[i] == 0:
                if temp[i-1] == 0:
                    if temp[i-2] == 0:
                        if temp[i-3] == 0:
                            temp[i] = temp[i-3]
                            temp[i-3] = 0
                        else:
                            temp[i] = temp[i-3]
                            temp[i-3] = 0
                    else:
                        temp[i] = temp[i-2]
                        temp[i-2] = 0
                else:
                    temp[i] = temp[i-1]
                    temp[i-1] = 0
        for j in range (3,-1,-1):
            if temp[j] == temp[j-1]:
                temp[j] += temp[j-1]
                temp[j-1] = temp[j-2]
                temp[j-2] = temp[j-3]
                temp[j-3] = temp[j-4]
        for k in range (4):
            grid[k][colm] = temp[k]                                

"""Merge vales to the left"""           
def push_right (grid):
    for row in range (len(grid)):
            temp = [0,0,0,0,0,0,0,0]
            for colm in range(4):
                temp[colm] = grid[row][colm]
            for i in range (3,-1,-1):
                if temp[i] == 0:
                    if temp[i-1] == 0:
                        if temp[i-2] == 0:
                            if temp[i-3] == 0:
                                temp[i] = temp[i-3]
                                temp[i-3] = 0
                            else:
                                temp[i] = temp[i-3]
                                temp[i-3] = 0
                        else:
                            temp[i] = temp[i-2]
                            temp[i-2] = 0
                    else:
                        temp[i] = temp[i-1]
                        temp[i-1] = 0
            for j in range (3,-1,-1):
                if temp[j] == temp[j-1]:
                    temp[j] += temp[j-1]
                    temp[j-1] = temp[j-2]
                    temp[j-2] = temp[j-3]
                    temp[j-3] = temp[j-4]
            for k in range (4):
                grid[row][k] = temp[k]  
                
"""Merge values to the right"""
def push_left (grid):
    for row in range (len(grid)):
            temp = [0,0,0,0,0,0,0,0]
            for colm in range(4):
                temp[colm] = grid[row][colm]
            for i in range (4):
                if temp[i] == 0:
                    if temp[i+1] == 0:
                        if temp[i+2] == 0:
                            if temp[i+3] == 0:
                                temp[i] = temp[i+3]
                                temp[i+3] = 0
                            else:
                                temp[i] = temp[i+3]
                                temp[i+3] = 0
                        else:
                            temp[i] = temp[i+2]
                            temp[i+2] = 0
                    else:
                        temp[i] = temp[i+1]
                        temp[i+1] = 0
            for j in range (4):
                if temp[j] == temp[j+1]:
                    temp[j] += temp[j+1]
                    temp[j+1] = temp[j+2]
                    temp[j+2] = temp[j+3]
                    temp[j+3] = temp[j+4]
            for k in range (4):
                grid[row][k] = temp[k]  