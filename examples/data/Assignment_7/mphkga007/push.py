
def push_up(grid):
    
    for row in range(3,0,-1):
        for colunm in range(4):
            #checks if the the value in the grid is zero
            if grid[row][colunm]!=0:
                #checks if there is an empty space above the grid and if there is move it to the grid above
                if grid[row-1][colunm]==0:
                    grid[row-1][colunm]=grid[row][colunm]
                    grid[row][colunm]=0
                #checks if the number above the grid is equal to the one in the grid
                elif grid[row-1][colunm]==grid[row][colunm]:
                    grid[row-1][colunm]=2*grid[row][colunm] #if they are equal merge  them
                    if row<3:
                        if grid[row+1][colunm]!=0:  
                            grid[row][colunm]=grid[row+1][colunm]
                            grid[row+1][colunm]=0
                        elif grid[row+1][colunm]==0:
                            grid[row][colunm]=0 
                    else:
                        grid[row][colunm]=0

                    
def push_down(grid):
    for row  in range(3):
        for colunm in range(4):
            #checks if the the value in the grid is zero
            if grid[row][colunm]!=0:
                #checks if the grid below is an empty space or not
                        if grid[row+1][colunm]==0: 
                            grid[row+1][colunm]=grid[row][colunm]
                            grid[row][colunm]=0
                        #checks if the grid below has same value as the grid
                        elif grid[row+1][colunm]==grid[row][colunm]:
                            grid[row+1][colunm]=2*grid[row][colunm]
                            #checks if the grid before the current one has an emptyspace or not
                            if grid[row-1][colunm]!=0:
                                grid[row][colunm]=grid[row-1][colunm]
                                grid[row-1][colunm]=0
                            elif grid[row-1][colunm]==0:
                                grid[row][colunm]=0  


#moves grid side ways
def push_left(grid):
    for colunm in range(3,0,-1):
        for row in range(4):
            #checks if the grid  is not equal to zero
            if grid[row][colunm]!=0:
                #checks if adjacent side are equal
            
                        if grid[row][colunm-1]==0:  #checks if the grid before has an empty space or not
                            grid[row][colunm-1]=grid[row][colunm]
                            grid[row][colunm]=0
                        elif grid[row][colunm-1]==grid[row][colunm]:
                            grid[row][colunm-1]=2*grid[row][colunm] #if the grid are equal merge
                            if grid[row][colunm+1]!=0:
                                grid[row][colunm]=grid[row][colunm+1]
                                grid[row][colunm+1]=0
                            elif grid[row][colunm+1]==0:
                                grid[row][colunm]=0  
                            
def push_right(grid):
    for colunm in range(3):
        for row in range(4):
            #checks if a grid has value or not
            if grid[row][colunm]!=0:
                        if grid[row][colunm+1]==0:
                            grid[row][colunm+1]=grid[row][colunm]
                            grid[row][colunm]=0
                        elif grid[row][colunm+1]==grid[row][colunm]:
                            grid[row][colunm+1]=2*grid[row][colunm] #merge the grid if they have the same value
                            if grid[row][colunm-1]!=0:
                                grid[row][colunm]=grid[row][colunm-1]
                                grid[row][colunm-1]=0
                            elif grid[row][colunm-1]==0:
                                grid[row][colunm]=0  

 
    
                 
                      
    
                

                            
                        
    
                                  
                                        
                        