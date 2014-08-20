#program to move values and play the game 2048
#Michael Field
#28 April 2014
import util

def push_up(grid):
    #merge grid values upwards
    for shifts in range(4):
        for row in range(4):
            for col in range(4):
                #check if current value is empty space
                if grid[row][col] == 0:
                    #move blovk below into the current block
                    if (row+1)<=3:
                        grid[row][col] = grid[row+1][col]
                        grid[row+1][col] = 0
                        
    #check adjacent values and merge values that are the same
    for row in range(4):
        for col in range(4):
            if (row+1)<=3:
                    #check to see if the number below is the same
                    if grid[row][col] == grid[row+1][col]:
                        #add the below number to the current number and replace the number below with a 0
                        grid[row][col] += grid[row+1][col]
                        grid[row+1][col] = 0
                        
    #merge grid values upwards
    for shifts in range(4):
        for row in range(4):
            for col in range(4):
                #check if current value is empty space
                if grid[row][col] == 0:
                    #move blovk below into the current block
                    if (row+1)<=3:
                        grid[row][col] = grid[row+1][col]
                        grid[row+1][col] = 0
                
                    
                
                        

def push_down(grid):
    #merge grid values downwards
    for shifts in range(4):
        for row in range(4):
            for col in range(4):
                #check if there is an empty space below the current grid value
                if grid[row][col] == 0:
                    #move current grid value into the block below it
                    if (row-1)>=0:
                        grid[row][col] = grid[row-1][col]
                        grid[row-1][col] = 0                   
                        
    #check adjacent values and merge values that are the same
    for row in range(4):
        for col in range(4):
            if (row-1)>=0:
                #check to see if the number below is the same
                if grid[row][col] == grid[row-1][col]:
                    #add the below number to the current number and replace the number above with a 0
                    grid[row][col] += grid[row-1][col]
                    grid[row-1][col] = 0
                    
    #merge grid values downwards
    for shifts in range(4):
        for row in range(4):
            for col in range(4):
                #check if there is an empty space below the current grid value
                if grid[row][col] == 0:
                    #move current grid value into the block below it
                    if (row-1)>=0:
                        grid[row][col] = grid[row-1][col]
                        grid[row-1][col] = 0

      
                    
def push_left(grid): 
    #merge grid values left
    for shifts in range(4):
        for row in range(4):
            for col in range(4):
                #check if there is an empty space left of the current grid value
                if grid[row][col] == 0:
                    #move current grid value into the block left of it
                    if (col+1)<=3:
                        grid[row][col] = grid[row][col+1]
                        grid[row][col+1] = 0
                    else:
                        grid[row][col] = 0                    
                        
    #check adjacent values and merge values that are the same
    for row in range(4):
        for col in range(4):
            if (col+1)<=3:
                #check to see if the number left is the same
                if grid[row][col] == grid[row][col+1]:
                    #add the below number to the current number and replace the number right with a 0
                    grid[row][col] += grid[row][col+1]
                    grid[row][col+1] = 0  
                        
                        
    #merge grid values left
    for shifts in range(4):
        for row in range(4):
            for col in range(4):
                #check if there is an empty space left of the current grid value
                if grid[row][col] == 0:
                    #move current grid value into the block left of it
                    if (col+1)<=3:
                        grid[row][col] = grid[row][col+1]
                        grid[row][col+1] = 0
                        


def push_right(grid):
    
    #merge grid values left
    for shifts in range(4):
        for row in range(4):
            for col in range(4):
                #check if the current grid value is zero
                if grid[row][col] == 0:
                    #move grid value of the block left of the current block, to the current block
                    if (col-1)>=0:
                        grid[row][col] = grid[row][col-1]
                        grid[row][col-1] = 0
                    else:
                        grid[row][col] = 0                      
                        
    #check adjacent values and merge values that are the same
    for row in range(4):
        for col in range(4):
            if (col-1)>=0:
                #check to see if the number left is the same
                if grid[row][col] == grid[row][col-1]:
                    #add the below number to the current number and replace the number left with a 0
                    grid[row][col-1]  += grid[row][col]
                    grid[row][col] = 0
                    
    #merge grid values left
    for shifts in range(4):
        for row in range(4):
            for col in range(4):
                #check if the current grid value is zero
                if grid[row][col] == 0:
                    #move grid value of the block left of the current block, to the current block
                    if (col-1)>=0:
                        grid[row][col] = grid[row][col-1]
                        grid[row][col-1] = 0
                    