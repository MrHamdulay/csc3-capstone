""" Charles Schleich-SCHCHA027
2014-May-01
"""
import util

def push_up (grid):
#merges grid values upwards
    # code test for 3 different cases with varying spaces between equal numbers
    for row in range(4):
        for col in range(4):
            helptest=True
            if row!=3:
                if grid[row+1][col] == grid[row][col]:
                    grid[row][col]*=2
                    grid[row+1][col]=0
                    helptest=False
                elif row==0 or row==1:
                    if grid[row+1][col]==0 and grid[row+2][col]==grid[row][col]:
                        grid[row][col]*=2
                        grid[row+2][col]=0
                        helptest=False
                if row==0 and helptest==True:
                    if grid[row+1][col]==0 and grid[row+2][col]==0 and grid[row+3][col]==grid[row][col]:
                        grid[row][col]*=2
                        grid[row+3][col]=0
 
     #Shifts the unshifted values into correct place    
    for shift in range(4):
        for row in reversed(range(4)):
            for col in reversed(range(4)):
                if row!=0:
                    if grid[row-1][col] == 0:
                        grid[row-1][col] = grid[row][col]
                        grid[row][col]=0
                    

            
                    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////           
            

def push_down (grid):
#merges grid values Downwards
       # code test for 3 different cases with varying spaces between equal numbers
    for row in reversed(range(4)):
           for col in reversed(range(4)):
               helptest=True
               if row!=0:
                   if grid[row][col] == grid[row-1][col]:
                       grid[row][col]*=2
                       grid[row-1][col]=0
                       helptest=False
                   elif row==3 or row==2 :
                       if grid[row-1][col]==0 and grid[row-2][col]==grid[row][col]:
                           grid[row][col]*=2
                           grid[row-2][col]=0
                           helptest=False
                   if row==3 and helptest==True:
                       if grid[row-1][col]==0 and grid[row-2][col]==0 and grid[row-3][col]==grid[row][col]:
                           grid[row][col]*=2
                           grid[row-3][col]=0
                            
     #Shifts the unshifted values into correct place
    for shift in range(4):
        for row in range(4):
            for col in range(4):
                if row!=3:
                    if grid[row+1][col] == 0:
                        grid[row+1][col] = grid[row][col]
                        grid[row][col]=0    


    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    
def push_left (grid):
#merges grid values left
       # code test for 3 different cases with varying spaces between equal numbers
    for row in range(4):
            for col in range(4):
                helptest=True
                if col!=3:
                    if grid[row][col] == grid[row][col+1]:
                        grid[row][col]*=2
                        grid[row][col+1]=0
                        helptest=False
                    elif col==0 or col==1:
                        if grid[row][col+1]==0 and grid[row][col+2]==grid[row][col]:
                            grid[row][col]*=2
                            grid[row][col+2]=0
                            helptest=False
                    if col==0 and helptest==True:
                        if grid[row][col+1]==0 and grid[row][col+2]==0 and grid[row][col+3]==grid[row][col]:
                            grid[row][col]*=2
                            grid[row][col+3]=0
                               
                       
                            #Shifts the unshifted values into correct place
    for shift in range(4):
        for row in reversed(range(4)):
            for col in reversed(range(4)):
                if col!=0:
                    if grid[row][col-1] == 0:
                        grid[row][col-1] = grid[row][col]
                        grid[row][col]=0      
    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def push_right (grid):
    #merges grid values right
       # code test for 3 different cases with varying spaces between equal numbers
    for row in reversed(range(4)):
               for col in reversed(range(4)):
                   helptest=True
                   if col!=0:
                       if grid[row][col]==grid[row][col-1]:
                           grid[row][col]*=2
                           grid[row][col-1]=0
                           helptest=False
                       elif col==3 or col==2:
                           if grid[row][col-1]==0 and grid[row][col]==grid[row][col-2]:
                                grid[row][col]*=2
                                grid[row][col-2]=0
                                helptest=False
                       if col==0 and helptest==True:
                           if grid[row][col-1]==0 and grid[row][col-2]==0 and grid[row][col]==grid[row][col-3]:
                               grid[row][col]*=2
                               grid[row][col-3]=0
                               

     #Shifts the unshifted values into correct place
    for shift in range(4):
        for row in range(4):
            for col in range(4):
                if col!=3:
                    if grid[row][col+1] == 0:
                        grid[row][col+1] = grid[row][col]
                        grid[row][col]=0      
                       