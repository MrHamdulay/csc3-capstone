"""Tofunmi Olagoke
29 April 2014
2048 game functions"""

def push_down (grid):
    #Merges numbers down
    
#removes the spaces in between the numbers
    for i in range (4):
        for list in range(1,4):
            
#adds adjacent equal numbers and removes further spaces created from this
            for column in range (4): 
                if grid[list][column]==0:
                    grid[list][column]=grid[list-1][column]
                    grid[list-1][column]=0 


    for list in range(1,4):
        for column in range (4): 

                if grid[list][column]==grid[list-1][column] or grid[list][column]==0:
                    grid[list][column]=grid[list][column]*2
                    grid[list-1][column]=0

    return grid

def push_up (grid):
    #Merges numbers up
        
#removes the spaces in between the numbers   
    for i in range (4):
        for list in range(2,-1,-1):
            for column in range (3,-1,-1): 
                if grid[list][column]==0:
                    grid[list][column]=grid[list+1][column]
                    grid[list+1][column]=0 
                else:
                    grid[list][column]=grid[list][column]
                    grid[list+1][column]=grid[list+1][column] 
    for i in range (4):
        for list in range(2,-1,-1):
            for column in range (3,-1,-1): 
#adds adjacent equal numbers and removes further spaces created from this
                if grid[list][column]==grid[list+1][column] or grid[list][column]==0:
                    grid[list][column]=grid[list][column]*2
                    grid[list+1][column]=0

    return grid

def push_right (grid):
#Merges numbers right
        
#removes the spaces in between the numbers   
    for i in range (4):
        for list in range(4):
            for column in range (1,4): 
                if grid[list][column]==0:
                    grid[list][column]=grid[list][column-1]
                    grid[list][column-1]=0 

    for i in range (4):
        for list in range(4):
            for column in range (1,4): 
                
#adds adjacent equal numbers and removes further spaces created from this
                    if grid[list][column]==grid[list][column-1] or grid[list][column]==0:
                        grid[list][column]=grid[list][column]*2
                        grid[list][column-1]=0

    return grid

def push_left (grid):
    #Merges numbers left
        
#removes the spaces in between the numbers   
    for i in range (4):
        for list in range(3,-1,-1):
            for column in range (2,-1,-1): 
                if grid[list][column]==0:
                    grid[list][column]=grid[list][column+1]
                    grid[list][column+1]=0 

    for i in range (4):
        for list in range(3,-1,-1):
            for column in range (2,-1,-1): 
#adds adjacent equal numbers and removes further spaces created from this
                if grid[list][column]==grid[list][column+1] or grid[list][column]==0:
                    grid[list][column]=grid[list][column]*2
                    grid[list][column+1]=0
    return grid