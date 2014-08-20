"""Mphuthi Mamorena 
Assignment 7
Quetion 3"""

def push_left(grid):
    for row in range(4):
        for col in range(4):
            # summming the adjecent numbers
            if 0<=col<3:
                if grid[row][col]==grid[row][col+1]:
                    grid[row][col]+=grid[row][col+1]
                    grid[row][col+1]=0
                    
    for row in range(4):
        for col in range(4):    
            if 0<=col<3:      
                if grid[row][0]==0:#eleminatind gaps for the first column
                    if grid[row][1]!=0:
                        grid[row][0]=grid[row][1]
                        grid[row][1]=0
                    elif grid[row][2]!=0:
                        grid[row][0]=grid[row][2]
                        grid[row][2]=0
                    elif grid[row][3]!=0:
                        grid[row][0]=grid[row][3]
                        grid[row][3]=0                  
                elif grid[row][1]==0:#eleminatind gaps for the second column
                    if grid[row][2]!=0:
                        grid[row][1]=grid[row][2]
                        grid[row][2]=0
                    elif grid[row][3]!=0:
                        grid[row][1]=grid[row][3]
                        grid[row][3]=0 
                    if grid[row][0]==grid[row][1]:
                        grid[row][0]+=grid[row][1]
                        grid[row][1]=0                    
                elif grid[row][2]==0:#eleminatind gaps for the third column
                    if grid[row][3]!=0:
                        grid[row][2]=grid[row][3]
                        grid[row][3]=0 
                    if grid[row][2]==grid[row][1]:
                        grid[row][1]+=grid[row][2]
                        grid[row][2]=0                    
    # check if thre are still gaps 
    for row in range(4):
        for col in range(4):    
            if 0<=col<3:      
                if grid[row][0]==0:
                    if grid[row][1]!=0:
                        grid[row][0]=grid[row][1]
                        grid[row][1]=0
                    elif grid[row][2]!=0:
                        grid[row][0]=grid[row][2]
                        grid[row][2]=0
                    elif grid[row][3]!=0:
                        grid[row][0]=grid[row][3]
                        grid[row][3]=0   
                elif grid[row][1]==0:
                    if grid[row][2]!=0:
                        grid[row][1]=grid[row][2]
                        grid[row][2]=0
                    elif grid[row][3]!=0:
                        grid[row][1]=grid[row][3]
                        grid[row][3]=0  
                elif grid[row][2]==0:
                    if grid[row][3]!=0:
                        grid[row][2]=grid[row][3]
                        grid[row][3]=0         
    return grid



def push_up(grid):
    for row in range(4):
        for col in range(4):
            if 0<=col<3:# summming the adjecent numbers up 
                if grid[row][col]==grid[row-1][col]:
                    grid[row-1][col]+=grid[row][col]
                    grid[row][col]=0
    #elminante gaps
    for row in range(4):
        for col in range(4):    
            if 0<=col<=3:     
                if grid[0][col]==0:#eleminatind gaps for the first row
                    if grid[1][col]!=0:
                        grid[0][col]=grid[1][col]
                        grid[1][col]=0
                    elif grid[2][col]!=0:
                        grid[0][col]=grid[2][col]
                        grid[2][col]=0
                    elif grid[3][col]!=0:
                        grid[0][col]=grid[3][col]
                        grid[3][col]=0                      
                elif grid[1][col]==0:#eleminatind gaps for the second row
                    if grid[2][col]!=0:
                        grid[1][col]=grid[2][col]
                        grid[2][col]=0
                    elif grid[3][col]!=0:
                        grid[1][col]=grid[3][col]
                        grid[3][col]=0
                    if grid[1][col]==grid[0][col]:
                        grid[0][col]+=grid[1][col]
                        grid[1][col]=0                    
                elif grid[2][col]==0:#eleminatind gaps for the third
                    if grid[3][col]!=0:
                        grid[2][col]=grid[3][col]
                        grid[3][col]=0 
                    if grid[2][col]==grid[1][col]:
                        grid[1][col]+=grid[2][col]
                        grid[2][col]=0                     
    #checking for gaps again
    for row in range(4):
        for col in range(4):    
            if 0<=col<=3:      
                if grid[0][col]==0:
                    if grid[1][col]!=0:
                        grid[0][col]=grid[1][col]
                        grid[1][col]=0
                    elif grid[2][col]!=0:
                        grid[0][col]=grid[2][col]
                        grid[2][col]=0
                    elif grid[3][col]!=0:
                        grid[0][col]=grid[3][col]
                        grid[3][col]=0   
                elif grid[1][col]==0:
                    if grid[2][col]!=0:
                        grid[1][col]=grid[2][col]
                        grid[2][col]=0
                    elif grid[3][col]!=0:
                            grid[1][col]=grid[3][col]
                            grid[3][col]=0  
                elif grid[2][col]==0:
                    if grid[3][col]!=0:
                        grid[2][col]=grid[3][col]
                        grid[3][col]=0     
            
                        
        return grid

def push_down(grid):
    for row in range(4):
        for col in range(4):
            if 0<=row<3:#summing the adjencent numbers 
                if grid[row][col]==grid[row+1][col]:
                    grid[row+1][col]+=grid[row][col]
                    grid[row][col]=0
    for row in range(4):
        for col in range(4):    
            if 0<=col<3:      
                if grid[3][col]==0:#eleminatind gaps for the forth row
                    if grid[2][col]!=0:
                        grid[3][col]=grid[2][col]
                        grid[2][col]=0
                    elif grid[1][col]!=0:
                        grid[3][col]=grid[1][col]
                        grid[1][col]=0
                    elif grid[0][col]!=0:
                        grid[3][col]=grid[0][col]
                        grid[0][col]=0
                                       
                elif grid[2][col]==0:#eleminatind gaps for the third row 
                    if grid[1][col]!=0:
                        grid[2][col]=grid[1][col]
                        grid[1][col]=0
                    elif grid[0][col]!=0:
                        grid[2][col]=grid[0][col]
                        grid[0][col]=0  
                    if grid[2][col]==grid[3][col]:
                        grid[3][col]+=grid[2][col]
                        grid[2][col]=0                     
                elif grid[1][col]==0:#eleminatind gaps for the second row
                    if grid[0][col]!=0:
                        grid[1][col]=grid[0][col]
                        grid[0][col]=0 
                    if grid[1][col]==grid[2][col]:
                        grid[2][col]+=grid[1][col]
                        grid[1][col]=0                    
    #eliminating gaps again
    for row in range(4):
        for col in range(4):    
            if 0<=col<3:      
                if grid[3][col]==0:
                    if grid[2][col]!=0:
                        grid[3][col]=grid[2][col]
                        grid[2][col]=0
                    elif grid[1][col]!=0:
                        grid[3][col]=grid[1][col]
                        grid[1][col]=0
                    elif grid[0][col]!=0:
                        grid[3][col]=grid[0][col]
                        grid[0][col]=0   
            elif grid[2][col]==0:
                if grid[1][col]!=0:
                    grid[2][col]=grid[1][col]
                    grid[1][col]=0
                elif grid[0][col]!=0:
                    grid[2][col]=grid[0][col]
                    grid[0][col]=0  
            elif grid[1][col]==0:
                if grid[0][col]!=0:
                    grid[1][col]=grid[0][col]
                    grid[0][col]=0
    return grid

def push_right(grid):
    #checking for equal adjecent values 
        for row in range(4):
            for col in range(4):
                if 0<=col<3:#summing the adjecent numbers 
                    if grid[row][col]==grid[row][col-1]:
                        grid[row][col]+=grid[row][col-1]
                        grid[row][col-1]=0
        for row in range(4):
            for col in range(4):    
                if 0<=col<=3:      
                    if grid[row][3]==0:#eleminatind gaps for the forth column
                        if grid[row][2]!=0:
                            grid[row][3]=grid[row][2]
                            grid[row][2]=0
                        elif grid[row][1]!=0:
                            grid[row][3]=grid[row][1]
                            grid[row][1]=0
                        elif grid[row][0]!=0:
                            grid[row][3]=grid[row][0]
                            grid[row][0]=0   
                    elif grid[row][2]==0:#eleminatind gaps for the third column
                        if grid[row][1]!=0:
                            grid[row][2]=grid[row][1]
                            grid[row][1]=0
                        elif grid[row][0]!=0:
                            grid[row][2]=grid[row][0]
                            grid[row][0]=0 
                        if grid[row][2]==grid[row][3]:
                            grid[row][3]+=grid[row][2]
                            grid[row][2]=0                     
                    elif grid[row][1]==0:#eleminatind gaps for the second  column
                        if grid[row][0]!=0:
                            grid[row][1]=grid[row][0]
                            grid[row][0]=0 
                        if grid[row][1]==grid[row][2]:
                            grid[row][2]+=grid[row][1]
                            grid[row][1]=0 
        #checking for gaps again
        for row in range(4):
            for col in range(4):
                if 0<=col<3:
                    if grid[row][col]==grid[row][col-1]:
                        grid[row][col]+=grid[row][col-1]
                        grid[row][col-1]=0
        for row in range(4):
            for col in range(4):    
                if 0<=col<=3:      
                    if grid[row][3]==0:
                        if grid[row][2]!=0:
                            grid[row][3]=grid[row][2]
                            grid[row][2]=0
                        elif grid[row][1]!=0:
                            grid[row][3]=grid[row][1]
                            grid[row][1]=0
                        elif grid[row][0]!=0:
                            grid[row][3]=grid[row][0]
                            grid[row][0]=0   
                    elif grid[row][2]==0:
                        if grid[row][1]!=0:
                            grid[row][2]=grid[row][1]
                            grid[row][1]=0
                        elif grid[row][0]!=0:
                            grid[row][2]=grid[row][0]
                            grid[row][0]=0  
                    elif grid[row][1]==0:
                        if grid[row][0]!=0:
                            grid[row][1]=grid[row][0]
                            grid[row][0]=0  
    
                
                    
       
        return grid