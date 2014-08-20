"""Functions for 2048 game
Tauhirah Eguardo
5/1/2014"""


def push_up (grid):
    """merge grid values upwards"""
    # needs to check if values are "0" or the same and check if the next values
    
    #create new matrix grouping columns instead of rows.
    new_grid = []
    col = []
    for y in range(4):
        for x in range(4):
            col.append(grid[x][y])
        new_grid.append(col)
        col = []
    print(new_grid)
    #start from top and compare with lower, and add together or move lower to to upper position
    for i in range(4):
        for j in range(3,-1,-1):
            if new_grid[i][j-1] == 0 and j >= 1:
                new_grid[i][j-1] = new_grid[i][j]
                new_grid[i][j] = 0
                if new_grid[i][j-2] == 0 and j >=2:
                    new_grid[i][j-2] = new_grid[i][j-1]
                    new_grid[i][j-1] = 0
                    if new_grid[i][j-3] == 0 and j >=3:
                        new_grid[i][j-3] = new_grid[i][j-2]
                        new_grid[i][j-2] = 0                            
                            
    for i in range(4):
        for j in range(3,-1,-1):                
            if new_grid[i][j] == new_grid[i][j-1]:
                new_grid[i][j-1] = (new_grid[i][j])+(new_grid[i][j])
                new_grid[i][j] = 0
            else: 
                pass
    print(new_grid)
    
    
    
def push_down (grid):
    new_grid = []
    col = []
    for y in range(4):
        for x in range(4):
            col.append(grid[x][y])
        new_grid.append(col)
        col = []
    print(new_grid)    
    
    
    for i in range(4):
        if 0 in new_grid[i]:
            high = new_grid.count(0) - 1
            while new_grid[i][0] != 0 and new_grid[i][high] != 0:
                for j in range(3,-1,-1):
                    #if new_grid[i][j] == 0 and j > 0:
                        #new_grid[i][j] = new_grid[i][j-1]
                        #new_grid[i][j-1] = 0
                    
                    if new_grid[i][j-1] == 0 and j >= 1:
                        new_grid[i][j-1] = new_grid[i][j]
                        new_grid[i][j] = 0
                        if new_grid[i][j-2] == 0 and j >=2:
                            new_grid[i][j-2] = new_grid[i][j-1]
                            new_grid[i][j-1] = 0
                            if new_grid[i][j-3] == 0 and j >3:
                                new_grid[i][j-3] = new_grid[i][j-2]
                                new_grid[i][j-2] = 0                      
                         
                        
    for i in range(4):
        for j in range(3):                
            if new_grid[i][j] == new_grid[i][j+1]:
                new_grid[i][j+1] = (new_grid[i][j])+(new_grid[i][j])
                new_grid[i][j] = 0
            else: 
                pass
             
    print(new_grid)        


grid = [[64,32,32,2],[64,4,2,0],[4,2,2,0],[2,0,0,2]]

push_down(grid)
