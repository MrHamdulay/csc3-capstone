#Done By Guy Green
#Functions for the game 2048 ie: Push the numbers up or down
#Assignment 7 Question 3
 

def push_up (grid): 
    """It combines like grid values upwards and moves values upwards"""
    #Pushing the value up to the highest empty space ie: the value is 0 
    for a in range (4): 
        for i in range(3,0,-1): 
            for j in range(4): 
                if grid[i-1][j]==0: 
                    grid[i-1][j]=grid[i][j] 
                    grid[i][j]=0
    
    #Combining like values. Starting at the top moving downward to see if there are similar terms
    for i in range(3): 
        for j in range(4):         
            if grid[i][j]==grid[i+1][j]: 
                grid[i][j]=(grid[i][j])*2
                grid[i+1][j]=0
    
    #Pushing the value up to the highest empty space (ie: the value is 0 ) after the combination because it combines values downwards leaving empty spaces above           
    for a in range (4): 
        for i in range(3,0,-1): 
            for j in range(4): 
                if grid[i-1][j]==0: 
                    grid[i-1][j]=grid[i][j] 
                    grid[i][j]=0 


def push_down (grid): 
    """It combines like grid values downwards and moves values downwards"""
    #Pushing the value down to the lowest empty space ie: the value is 0 
    for a in range(4): 
        for i in range(2,-1,-1): 
            for j in range(4): 
                if grid[i+1][j]==0: 
                    grid[i+1][j]=grid[i][j] 
                    grid[i][j]=0
                      
    #Combining like values. Starting at the bottom moving upward to see if there are similar terms
    for i in range(2,-1,-1): 
        for j in range(4): 
            if grid[i][j]==grid[i+1][j]: 
                grid[i+1][j]=(grid[i+1][j])*2
                grid[i][j]=0
    
    #Pushing the value down to the lowest empty space (ie: the value is 0 ) after the combination because it combines values upwards leaving empty spaces below              
    for a in range(4): 
        for i in range(2,-1,-1): 
            for j in range(4): 
                if grid[i+1][j]==0: 
                    grid[i+1][j]=grid[i][j] 
                    grid[i][j]=0   
                      
def push_left (grid): 
    """It combines like grid values to the left and moves values to the left"""
   #Works the same way as the push up and push down function (except to the left obviously)
    for a in range(4): 
        for i in range(4):  
            for j in range(3,0,-1):  
                if grid[i][j-1]==0: 
                    grid[i][j-1]=grid[i][j] 
                    grid[i][j]=0
                      
    for i in range(4): 
        for j in range(3):  
            if grid[i][j]==grid[i][j+1]: 
                grid[i][j]=(grid[i][j])*2
                grid[i][j+1]=0    
                                     
    for a in range(4): 
        for i in range(4):  
            for j in range(3,0,-1):  
                if grid[i][j-1]==0: 
                    grid[i][j-1]=grid[i][j] 
                    grid[i][j]=0
              
def push_right (grid): 
    """It combines like grid values to the right and moves values to the right"""    
    #Works the same way as the push up and push down function (except to the right obviously)
    for a in range(4): 
        for i in range(4): 
            for j in range(3):  
                if grid[i][j+1]==0: 
                    grid[i][j+1]=grid[i][j] 
                    grid[i][j]=0
    for i in range(4): 
            for j in range(3,0,-1):  
                if grid[i][j]==grid[i][j-1]: 
                    grid[i][j]=(grid[i][j])*2
                    grid[i][j-1]=0
    for a in range(4): 
        for i in range(4): 
            for j in range(3):  
                if grid[i][j+1]==0: 
                    grid[i][j+1]=grid[i][j] 
                    grid[i][j]=0