'''module for merging values in 4x4 grid
nasreen hoosain
02/05/2014'''


def push_left (grid):
    """merge grid values left"""  
    for i in range(4):
            grid[i] = merge_list(grid[i])
    return grid

def push_right (grid):
    """merge grid values right"""  
    #reverse rows
    for row in range(4):
        grid[row] = grid[row][::-1]
    new_grid = push_left(grid) #push grid left
    #re-reverse rows
    for i in range(4):
        new_grid[i] = new_grid[i][::-1]
        
    return new_grid       
            
def push_up (grid):
    """merge grid values upwards"""
    new_grid = [[],[],[],[]]
    #turn columns into rows
    for col in range (4):
        new_grid[col] = [grid[0][col], grid[1][col], grid[2][col], grid[3][col]]
    new_grid = push_left(new_grid) #merge grid left
    #turn rows back into columns
    for i in range(4):
        grid[i] = [new_grid[0][i], new_grid[1][i], new_grid[2][i], new_grid[3][i]]
    
    return grid

def push_down (grid):
    """merge grid values downwards""" 
    new_grid = [[],[],[],[]]
    #turn columns into rows 
    for col in range (4):
        new_grid[col] = [grid[0][col], grid[1][col], grid[2][col], grid[3][col]]
    new_grid = push_right(new_grid) #merge grid right
    #turn rows back into columns
    for i in range(4):
        grid[i] = [new_grid[0][i], new_grid[1][i], new_grid[2][i], new_grid[3][i]]
    return grid    
            
#function to merge a list of values
def merge_list (l):
    for j in range (3):
        for i in range(2, -1 + j, -1): #merge from back of list in steps
            if l[i] == 0 or l[i] == l[i+1]: #if current number = 0 or next number, merge with next number
                l[i] += l[i+1]
                l[i+1] = 0        #set next number = 0
    return l             