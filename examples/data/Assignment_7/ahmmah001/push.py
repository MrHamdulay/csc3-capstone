'''Program for moving in 2048
Mahnoor Ahmed
2 May 2014'''

import util
def push_right(grid):
    #new_grid= util.copy_grid (grid)
    empt_grid=[]
    #grid.append([" "]*4)
    i=0
    for j in range(4):
        if grid[i][j] >0:
            empt_grid.append([grid[i][j]])
        elif grid[i][j] == 0:
            if grid[i+1][j] > 0:
                empt_grid.append([grid[i+1][j]])
            elif grid[i+2][j] > 0:
                empt_grid.append([grid[i+2][j]])
            elif grid[i+3][j] >0:
                empt_grid.append([grid[i+3][j]])
    return(empt_grid)
                                
    
    
    #for i in range(4):
        #for j in range(4):
            #if grid[i][j] == 0:
                #if grid[i+1][j] > 0:
                    #empt_grid.append(grid[i+1][j])
                #elif grid[i+1][j] == 0 and grid[i+2][j] >0:
                    #empt_grid.append(grid[i+2][j])
                    ##empt_grid.insert(grid[i][j],grid[i+2][j])
                #elif grid[i+2] == 0 and grid[i+3][j] > 0:
                    #empt_grid.append(grid[i+3][j])
                    ##empt_grid.insert(grid[i][j],grid[i+3][j])
    #grid=empt_grid
    #return(grid)
                