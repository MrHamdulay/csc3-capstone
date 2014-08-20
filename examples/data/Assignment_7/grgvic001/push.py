#simulation of merge functions from the game 2048
#victor gueorguiev
#27 april 2014

#use list.pop(..) if an element is NOT zero and then add it to the top/bottom/left/right of the list
def push_up (grid):
    """merge grid values upwards"""
    for i in range(len(grid)):
        freespot = 0
        for q in range(len(grid[i])):
            if grid[q][i] != 0:
                temp = grid[freespot][i]    #perform a swap using a temporary variable
                grid[freespot][i] = grid[q][i]
                grid[q][i] = temp
                freespot += 1
        for q in range(len(grid[i])-1):
            if grid[q][i] == grid[q+1][i]:
                grid[q][i] += grid[q+1][i]
                grid[q+1][i] = 0 
        freespot = 0
        for q in range(len(grid[i])):
            if grid[q][i] != 0:
                temp = grid[freespot][i]    #perform a swap using a temporary variable
                grid[freespot][i] = grid[q][i]
                grid[q][i] = temp
                freespot += 1   

def push_down (grid):
    """merge grid values downwards"""
    for i in range(len(grid)):
        freespot = len(grid[i])-1
        for q in range(len(grid[i])-1,-1,-1):
            if grid[q][i] != 0:
                temp = grid[freespot][i]    #perform a swap using a temporary variable
                grid[freespot][i] = grid[q][i]
                grid[q][i] = temp
                freespot += -1
        for q in range(len(grid[i])-1,0,-1):
            if grid[q][i] == grid[q-1][i]:
                grid[q][i] += grid[q-1][i]
                grid[q-1][i] = 0 
        freespot = len(grid[i])-1
        for q in range(len(grid[i])-1,-1,-1):
            if grid[q][i] != 0:
                temp = grid[freespot][i]    #perform a swap using a temporary variable
                grid[freespot][i] = grid[q][i]
                grid[q][i] = temp
                freespot += -1  

def push_left (grid):
    """merge grid values left"""
    for i in range(len(grid)):
        freespot = 0
        for q in range(len(grid[i])):
            if grid[i][q] != 0:
                temp = grid[i][freespot]    #perform a swap using a temporary variable
                grid[i][freespot] = grid[i][q]
                grid[i][q] = temp
                freespot += 1
        for q in range(len(grid[i])-1):
            if grid[i][q] == grid[i][q+1]:
                grid[i][q] += grid[i][q+1]
                grid[i][q+1] = 0 
        freespot = 0
        for q in range(len(grid[i])):
            if grid[i][q] != 0:
                temp = grid[i][freespot]    #perform a swap using a temporary variable
                grid[i][freespot] = grid[i][q]
                grid[i][q] = temp
                freespot += 1 

def push_right (grid):
    """merge grid values right"""
    for i in range(len(grid)):
        freespot = len(grid[i])-1
        for q in range(len(grid[i])-1,-1,-1):
            if grid[i][q] != 0:
                temp = grid[i][freespot]    #perform a swap using a temporary variable
                grid[i][freespot] = grid[i][q]
                grid[i][q] = temp
                freespot += -1
        for q in range(len(grid[i])-1,0,-1):
            if grid[i][q] == grid[i][q-1]:
                grid[i][q] += grid[i][q-1]
                grid[i][q-1] = 0 
        freespot = len(grid[i]) -1
        for q in range(len(grid[i])-1,-1,-1):
            if grid[i][q] != 0:
                temp = grid[i][freespot]    #perform a swap using a temporary variable
                grid[i][freespot] = grid[i][q]
                grid[i][q] = temp
                freespot += -1     