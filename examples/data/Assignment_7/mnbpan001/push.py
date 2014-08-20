"""Module containing code for 2048 game
Pankaj Munbodh
29 April 2014"""

# The following general algorithm was used to solve all of the following problems:
#1. The grid is read in a particular order and if a zero is found, all the values before it is pushed one level through the grid by keeping one of the coordinates of the grid fixed and moving through only the other coordinate(direction depends on what particular function is being used).
#2. After 1. , if the value is still zero, 1. is repeated. Note that since we are dealing with 4X4 grid, the number of times that  1. needs to be repeated is at most 3 times (when boundary value i.e. the particular row or column contains only one element which is 2 spaces from the zero value found). 
#3. If two numbers are the same next to each other (also in the appropriate positions), they are added (or final value=2*initial value since numbers are the same). The positions of each element within row or column then need to be re-adjusted again.
#Note1: A break statement is included to break out of inner loop so that program continues to look for zero values in another row/column (depending on function) because all corrections to the particular row/column have already been made. Or else, undesired operations might be repeated inside on the row/column. 
#Note2: Structure of code can be understood by looking at push_up function which has been commented extensively (the other functions are not commented to the same extent since they have the same structure and algorithm has already been supplied)
def push_up (grid):
    for j in range(4):
        for i in range(4):
            if grid[i][j]==0:      #checks for zero value
                
                for a in range(i,4):
                    if a==3:
                        grid[3][j]=0         #Here, j is fixed and i is varied to shift values of elements by assigning to each element the value just before it.
                    else:
                        grid[a][j]=grid[a+1][j]            # the zero value found is assigned to the bottom element of the column.
                
                if grid[i][j]==0:                  #second check for zero value
                    for a in range(i,4):
                        if a==3:
                            grid[3][j]=0
                        else:
                            grid[a][j]=grid[a+1][j]
                    
                    if grid[i][j]==0:               #third check for zero value
                        for a in range(i,4):
                            if a==3:
                                grid[3][j]=0
                            else:
                                grid[a][j]=grid[a+1][j]                        
                    
            
                if grid[0][j]==grid[1][j]:           #If two numbers are equal and in the appropriate positions, they are added together (or the new value is 2*old value). The positions need to be shifted again.  
                    grid[0][j]=2*grid[1][j]
                    grid[1][j]=grid[2][j]
                    grid[2][j]=0
                elif grid[1][j]==grid[2][j]:
                    grid[1][j]=2*grid[1][j]
                    grid[2][j]=grid[3][j]
                    grid[3][j]=0
                elif grid[2][j]==grid[3][j]:
                    grid[2][j]=2*grid[2][j]
                    grid[3][j]=0
            
                break                                # To proceed to next column
            elif grid[i][j]!=0 and i==3:
                if grid[0][j]==grid[1][j]:           #If two numbers are equal and in the appropriate positions, they are added together (or the new value is 2*old value). The positions need to be shifted again. Note: This set of operations is for when zero has not been found in the column. 
                    grid[0][j]=2*grid[1][j]
                    grid[1][j]=grid[2][j]
                    grid[2][j]=grid[3][j]
                    grid[3][j]=0
                elif grid[1][j]==grid[2][j]:
                    grid[1][j]=2*grid[1][j]
                    grid[2][j]=grid[3][j]
                    grid[3][j]=0
                elif grid[2][j]==grid[3][j]:
                    grid[2][j]=2*grid[2][j]
                    grid[3][j]=0                
                
                    
                    
def push_down(grid):
    for j in range(3,-1,-1):           #Main differences of structure of code from push_up(grid) are: 1. the grid is read in reverse. Note : Here, j is also fixed while i is varied(for inner 'for' loop). The rest of the structure of code is similar as above.
        for i in range(3,-1,-1):
            if grid[i][j]==0:
                    
                for a in range(i,-1,-1):
                    if a==0:
                        grid[0][j]=0
                    else:
                        grid[a][j]=grid[a-1][j]
                    
                if grid[i][j]==0:
                    for a in range(i,-1,-1):
                        if a==0:
                            grid[0][j]=0
                        else:
                            grid[a][j]=grid[a-1][j]
                        
                    if grid[i][j]==0:
                        for a in range(i,-1,-1):
                            if a==0:
                                grid[0][j]=0
                            else:
                                grid[a][j]=grid[a-1][j]                        
                        
                
                if grid[3][j]==grid[2][j]:
                    grid[3][j]=2*grid[3][j]
                    grid[2][j]=grid[1][j]
                    grid[1][j]=0
                elif grid[2][j]==grid[1][j]:
                    grid[2][j]=2*grid[2][j]
                    grid[1][j]=grid[0][j]
                    grid[0][j]=0
                elif grid[1][j]==grid[0][j]:
                    grid[1][j]=2*grid[1][j]
                    grid[0][j]=0
                break                                #Break out of inner loop to proceed to next column.
            elif grid[i][j]!=0 and i==0:    #Note: This set of operations is for when zero has not been found in the column. 
                if grid[3][j]==grid[2][j]:
                    grid[3][j]=2*grid[3][j]
                    grid[2][j]=grid[1][j]
                    grid[1][j]=grid[0][j]
                    grid[0][j]=0
                elif grid[2][j]==grid[1][j]:
                    grid[2][j]=2*grid[2][j]
                    grid[1][j]=grid[0][j]
                    grid[0][j]=0
                elif grid[1][j]==grid[0][j]:
                    grid[1][j]=2*grid[1][j]
                    grid[0][j]=0                
                
                    
def push_left(grid):                     #The grid is iterated through as in push_up (same sequence)
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                    
                for a in range(j,4):             #Here, i is fixed while j is varied.
            
                    if a==3:
                        grid[i][3]=0
                    else:
                        grid[i][a]=grid[i][a+1]
                    
                if grid[i][j]==0:
                    for a in range(j,4):
                        if a==3:
                            grid[i][3]=0
                        else:
                            grid[i][a]=grid[i][a+1]
                        
                    if grid[i][j]==0:
                        for a in range(j,4):
                            if a==3:
                                grid[i][3]=0
                            else:
                                grid[i][a]=grid[i][a+1]                        
                        
                
                if grid[i][0]==grid[i][1]:
                    grid[i][0]=2*grid[i][0]
                    grid[i][1]=grid[i][2]
                    grid[i][2]=0
                elif grid[i][1]==grid[i][2]:
                    grid[i][1]=2*grid[i][1]
                    grid[i][2]=grid[i][3]
                    grid[i][3]=0
                elif grid[i][2]==grid[i][3]:
                    grid[i][2]=2*grid[i][2]
                    grid[i][3]=0
                break                               #Break out of inner loop to proceed to next row.
            elif grid[i][j]!=0 and j==3:                #Note: This set of operations is for when zero has not been found in the column. 
                if grid[i][0]==grid[i][1]:
                    grid[i][0]=2*grid[i][0]
                    grid[i][1]=grid[i][2]
                    grid[i][2]=grid[i][3]
                    grid[i][3]=0
                elif grid[i][1]==grid[i][2]:
                    grid[i][1]=2*grid[i][1]
                    grid[i][2]=grid[i][3]
                    grid[i][3]=0
                elif grid[i][2]==grid[i][3]:
                    grid[i][2]=2*grid[i][2]
                    grid[i][3]=0                
                
                    
                    
def push_right(grid):                      #The grid is iterated through as in push_down
    for i in range(3,-1,-1):
            for j in range(3,-1,-1):
                if grid[i][j]==0:
                        
                    for a in range(j,-1,-1):                 #Here i is fixed while j is varied (of course for inner 'for' loop)
                        if a==0:
                            grid[i][0]=0
                        else:
                            grid[i][a]=grid[i][a-1]
                        
                    if grid[i][j]==0:
                        for a in range(j,-1,-1):
                            if a==0:
                                grid[i][0]=0
                            else:
                                grid[i][a]=grid[i][a-1]
                            
                        if grid[i][j]==0:
                            for a in range(j,-1,-1):
                                if a==0:
                                    grid[i][0]=0
                                else:
                                    grid[i][a]=grid[i][a-1]                        
                            
                    
                    if grid[i][3]==grid[i][2]:
                        grid[i][3]=2*grid[i][3]
                        grid[i][2]=grid[i][1]
                        grid[i][1]=0
                    elif grid[i][2]==grid[i][1]:
                        grid[i][2]=2*grid[i][2]
                        grid[i][1]=grid[i][0]
                        grid[i][0]=0
                    elif grid[i][1]==grid[i][0]:
                        grid[i][1]=2*grid[i][1]
                        grid[i][0]=0
                    break                                   #Break out of inner loop to proceed to next row.
                elif grid[i][j]!=0 and j==0:                #Note: This set of operations is for when zero has not been found in the column.    
                    if grid[i][3]==grid[i][2]:
                        grid[i][3]=2*grid[i][3]
                        grid[i][2]=grid[i][1]
                        grid[i][1]=grid[i][0]
                        grid[i][0]=0
                    elif grid[i][2]==grid[i][1]:
                        grid[i][2]=2*grid[i][2]
                        grid[i][1]=grid[i][0]
                        grid[i][0]=0
                    elif grid[i][1]==grid[i][0]:
                        grid[i][1]=2*grid[i][1]
                        grid[i][0]=0                    
                    
    
    