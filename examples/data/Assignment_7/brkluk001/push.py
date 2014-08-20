'''Program to complete the code for a 2048 program
30 April 2013
Luke Barker'''

def push_up (grid):    #must loop through list 3 times to make sure that numbers shift to the top
    for k in range(3):      #loop 3 times to ensure no spaces
        for i in range(1,4):
            for j in range(4):
                if grid[i-1][j] == 0:      #If the number above is a space/0 then shift up
                    grid[i-1][j] = grid[i][j] 
                    grid[i][j] =0    

    for i in range(1,4):
        for j in range(4):
            if grid[i-1][j] == grid[i][j]:    #as per game if the number are the same merge them with the merge in the top block
                grid[i-1][j] += grid[i][j]
                grid[i][j] = 0

    for i in range(1,4):     #repeat the first step to make sure all blocks shift up (no spaces)
        for j in range(4):
            if grid[i-1][j] == 0:
                grid[i-1][j] = grid[i][j]
                grid[i][j] =0     



def push_down (grid):
    for k in range(3): 
        for i in range(2,-1,-1):    #must loop through list 3 times to make sure that numbers shift to the bottom
            for j in range(4):      #loop 3 times to ensure no spaces
                if grid[i+1][j] ==0:   #If the number above is a space/0 then shift down
                    grid[i+1][j] = grid[i][j]
                    grid[i][j] = 0
                                    
    for i in range(2,-1,-1):
        for j in range(4):
            if grid[i+1][j] == grid[i][j]:    #as per game if the number are the same merge them with the merge in the bottom block
                grid[i+1][j] += grid[i][j]
                grid[i][j] =0
                                    
    for i in range(2,-1,-1):        #repeat the first step to make sure all blocks shift down (no spaces)
        for j in range(4): 
            if grid[i+1][j] ==0:
                grid[i+1][j] = grid[i][j]
                grid[i][j] = 0        
    

def push_left (grid):
    for k in range(3):
        for i in range(4):
            for j in range(1,4): #Same process as used in above functions except moving left
                if grid[i][j-1]==0:
                    grid[i][j-1] = grid[i][j]
                    grid[i][j] = 0
                                           
    for i in range(4):
        for j in range(1,4):
            if grid[i][j-1] == grid[i][j]:
                grid[i][j-1]+=grid[i][j]
                grid[i][j] =0
                                   
    for i in range(4):
        for j in range(1,4): 
            if grid[i][j-1]==0:
                grid[i][j-1] = grid[i][j]
                grid[i][j] = 0      

def push_right (grid):
    for k in range(3):
        for i in range(4):
            for j in range(2,-1,-1):     #same process as above functions except shifting to the right
                if grid[i][j+1] ==0:
                    grid[i][j+1] = grid[i][j]
                    grid[i][j] =0
                                           
    for i in range(4):
        for j in range(2,-1,-1):
            if grid[i][j+1] == grid[i][j]:
                grid[i][j+1]+=grid[i][j]
                grid[i][j]=0
                                   
    for i in range(4):
        for j in range(2,-1,-1): 
            if grid[i][j+1] ==0:
                grid[i][j+1] = grid[i][j]
                grid[i][j] =0                          