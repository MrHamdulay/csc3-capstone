import util
def push_up (grid):
    """merge grid values upwards"""
    for repeat in range(2):
        for i in range(4):
            for row in range(len(grid)):
                for column in range(len(grid[row])):
                    if(row != 0):
                        if(grid[row][column] != 0):
                            if(grid[row-1][column] == 0):
                                grid[row-1][column] = grid[row][column]
                                grid[row][column] = 0
        if(repeat == 0):
            for row in range(len(grid)):
                for column in range(len(grid[row])):
                    if(row != 0):
                        if(grid[row][column] != 0):
                            if(grid[row-1][column] == grid[row][column]):
                                grid[row-1][column] = grid[row][column]*2
                                grid[row][column] = 0        
    return grid
                

def push_down (grid):
    """merge grid values downwards"""

    for repeat in range(2):
        for i in range(4):
            for row in range(len(grid)-1,-1,-1):
                for column in range(len(grid)):
                    if(row != 3):
                        if(grid[row][column] != 0):
                            if(grid[row+1][column] == 0):
                                grid[row+1][column] = grid[row][column]
                                grid[row][column] = 0
        if(repeat == 0):
            for row in range(len(grid)-1,-1,-1):
                for column in range(len(grid[row])):
                    if(row != 3):
                        if(grid[row][column] != 0):
                            if(grid[row+1][column] == grid[row][column]):
                                grid[row+1][column] = grid[row][column]*2
                                grid[row][column] = 0        
    return grid    
    
    
    #grid = grid
    #for repeat in range(2):
        #for i in range(4):
            #for row in range(len(grid)):
                #for column in range(len(grid[row])):
                    #if(row != 3):
                        #if(grid[row][column] != 0):
                            #if(grid[row+1][column] == 0):
                                #grid[row+1][column] = grid[row][column]
                                #grid[row][column] = 0
        #if(repeat == 0):
            #for row in range(len(grid)):
                #for column in range(len(grid[row])):
                    #if(row != 3):
                        #if(grid[row][column] != 0):
                            #if(grid[row+1][column] == grid[row][column]):
                                #grid[row+1][column] = grid[row][column]*2
                                #grid[row][column] = 0  
        #grid = grid
                                
    #return grid    

def push_left (grid):
    """merge grid values left"""
    
    for repeat in range(2):
        for i in range(4):
            for row in range(len(grid)):
                for column in range(len(grid[row])):
                    if(column != 0):
                        if(grid[row][column] != 0):
                            if(grid[row][column-1] == 0):
                                grid[row][column-1] = grid[row][column]
                                grid[row][column] = 0
        if(repeat == 0):
            for row in range(len(grid)):
                for column in range(len(grid[row])):
                    if(column != 0):
                        if(grid[row][column] != 0):
                            if(grid[row][column-1] == grid[row][column]):
                                grid[row][column-1] = grid[row][column]*2
                                grid[row][column] = 0        
    return grid



def push_right (grid):
    """merge grid values right"""  
    
    for repeat in range(2):
        for i in range(4):
            for row in range(len(grid)):
                for column in range(len(grid)-1,-1,-1):
                    if(column != 3):
                        if(grid[row][column] != 0):
                            if(grid[row][column+1] == 0):
                                grid[row][column+1] = grid[row][column]
                                grid[row][column] = 0
        if(repeat == 0):
            for row in range(len(grid)):
                for column in range(len(grid)-1,-1,-1):
                    if(column != 3):
                        if(grid[row][column] != 0):
                            if(grid[row][column+1] == grid[row][column]):
                                grid[row][column+1] = grid[row][column]*2
                                grid[row][column] = 0        
    return grid



    
#util.print_grid(push_right([[8,4,4,0],[2,8,8,2],[8,4,2,8],[4,4,2,0]]))