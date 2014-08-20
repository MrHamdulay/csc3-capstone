"""Assignment 7 Question 3 2048 game  create merging functions
joshua wort
29 april 2014"""

#import util

def push_up(grid):
    """merge grid values upwards"""
    #run through grid 3 times so that all gaps are eliminated
    for loop in range(3):
        for row in range(3):
            for col in range(4):
                if grid[row][col]==0 or grid[row][col]==" ": # check if there is a gap
                    grid[row][col]=grid[row+1][col] #shift up and eliminate the gap 
                    grid[row+1][col]=0 
                    
    #if adjacent equal values merge together                
    for row in range(3):
        for col in range(4):
            if grid[row][col]==grid[row+1][col]:
                grid[row][col]=grid[row+1][col]*2
                grid[row+1][col]=0 
                
    #eliminate final gap maybe created by previous code            
    for row in range(3):
        for col in range(4):
            if grid[row][col]==0 or grid[row][col]==" ":
                grid[row][col]=grid[row+1][col]
                grid[row+1][col]=0
                
    #util.print_grid(grid)
    return 
    
def push_down(grid):
    """merge grid values downwards"""
    #run through grid 3 times so that all gaps are eliminated
    for loop in range(3):
            for row in range(2,-1,-1):
                for col in range(3,-1,-1):
                    if grid[row+1][col]==0 or grid[row+1][col]==" ":  # check if there is a gap
                        grid[row+1][col]=grid[row][col] #shift up and eliminate the gap
                        grid[row][col]=0
    
    #if adjacent equal values merge together                    
    for row in range(2,-1,-1):
        for col in range(3,-1,-1):
            if grid[row+1][col]==grid[row][col]:
                grid[row+1][col]=grid[row][col]*2
                grid[row][col]=0   
    
    #eliminate final gap maybe created by previous code                
    for row in range(2,-1,-1):
        for col in range(3,-1,-1):
            if grid[row+1][col]==0 or grid[row+1][col]==" ":
                grid[row+1][col]=grid[row][col]
                grid[row][col]=0
    return
    #util.print_grid(grid)    

def push_left(grid):
    """merge grid values left"""
    #repeat steps in push_up function but shift columns instead of rows
    for loop in range(3):
        for col in range(3):
            for row in range(4):
                if grid[row][col]==0 or grid[row][col]==" ":
                    grid[row][col]=grid[row][col+1]
                    grid[row][col+1]=0
    
    for col in range(3):
        for row in range(4):
            if grid[row][col]==grid[row][col+1]:
                grid[row][col]=grid[row][col+1]*2
                grid[row][col+1]=0
    
    for col in range(3):
        for row in range(4):
            if grid[row][col]==0 or grid[row][col]==" ":
                grid[row][col]=grid[row][col+1]
                grid[row][col+1]=0 
    #util.print_grid(grid)
    return

def push_right(grid):
    for loop in range(3):
        for col in range(2,-1,-1):
            for row in range(3,-1,-1):
                if grid[row][col+1]==0 or grid[row][col+1]==" ":
                    grid[row][col+1]=grid[row][col]
                    grid[row][col]=0
                    
    for col in range(2,-1,-1):
        for row in range(3,-1,-1):
            if grid[row][col+1]==grid[row][col]:
                grid[row][col+1]=grid[row][col]*2
                grid[row][col]=0    
                    
    for col in range(2,-1,-1):
        for row in range(3,-1,-1):
            if grid[row][col+1]==0 or grid[row][col+1]==" ":
                grid[row][col+1]=grid[row][col]
                grid[row][col]=0
    
    #util.print_grid(grid)
    return


#grid=[[2,0,2,2],[8,0,16,2],[2,0,8,2],[2,8,4,2]]
#push_right(grid)

        
                