"""Question 3 - push function
Jembe Moran
30 April 2014"""

def push_up(grid):
    for row in range(4):
        for col in range(4): #check every grid value
            if grid[row][col]==0:#if there is a 0, push up needs to occur (if empty space)
                if row<3: #if row not 3, take value from row below (if row is 3 there is no value below)
                    if grid[row+1][col] != 0:
                        grid[row][col]=grid[row+1][col]
                        grid[row+1][col]=0 #make bottom value 0
                    else: 
                        if row<2: #if row not 2 nor 3, take value from below, for taken value, replace with value below taken - (row+1) = (row+2)
                            if grid[row+2][col] != 0:
                                grid[row][col]=grid[row+2][col]
                                grid[row+2][col]=0 #make values with nothing 0
                                grid[row+1][col]=0
                            else:
                                if row<1: #if not 1,2,3, repeat movement thrice
                                    if grid[row+3][col] != 0:
                                        grid[row][col]=grid[row+3][col]
                                        grid[row+3][col]=0 #make values with nothing 0
                                        grid[row+2][col]=0 
                                        grid[row+1][col]=0
    for row in range(0,3):
        for col in range(4):
            if grid[row][col]!=0: #check if not 0
                if grid[row][col]==grid[row+1][col]: #check if value equal in row directly below
                    grid[row][col]=grid[row+1][col]+grid[row][col] #merge two values
                    if row==0: #same move up function as above
                        grid[row+1][col]=grid[row+2][col]
                        grid[row+2][col]=grid[row+3][col]
                        grid[row+3][col]=0
                    elif row==1:
                        grid[row+1][col]=grid[row+2][col]
                        grid[row+2][col]=0
                    elif row==2:
                        grid[row+1][col]=0
    return grid #returns altered grid
    
def push_down(grid): #same as move up, however row is checked in reverse order, and moved down (-) not up (+)
    for row in range(3,-1,-1):
        for col in range(4):
            if grid[row][col]==0:
                if row>0:
                    if grid[row-1][col] != 0:
                        grid[row][col]=grid[row-1][col]
                        grid[row-1][col]=0
                    else: 
                        if row>1:
                            if grid[row-2][col] != 0:
                                grid[row][col]=grid[row-2][col]
                                grid[row-2][col]=0
                                grid[row-1][col]=0
                            else:
                                if row>2:
                                    if grid[row-3][col] != 0:
                                        grid[row][col]=grid[row-3][col]
                                        grid[row-3][col]=0
                                        grid[row-2][col]=0
                                        grid[row-1][col]=0
    for row in range(3,0,-1):
        for col in range(4):
            if grid[row][col]!=0:
                if grid[row][col]==grid[row-1][col]:
                    grid[row][col]=grid[row-1][col]+grid[row][col]
                    if row==3:
                        grid[row-1][col]=grid[row-2][col]
                        grid[row-2][col]=grid[row-3][col]
                        grid[row-3][col]=0
                    elif row==2:
                        grid[row-1][col]=grid[row-2][col]
                        grid[row-2][col]=0
                    elif row==1:
                        grid[row-1][col]=0
    return grid 


def push_left(grid): #same as move up, however column is changed, not row
    for col in range(4):
        for row in range(4):
            if grid[row][col]==0:
                if col<3:
                    if grid[row][col+1] != 0:
                        grid[row][col]=grid[row][col+1]
                        grid[row][col+1]=0
                    else: 
                        if col<2:
                            if grid[row][col+2] != 0:
                                grid[row][col]=grid[row][col+2]
                                grid[row][col+2]=0
                                grid[row][col+1]=0
                            else:
                                if col<1:
                                    if grid[row][col+3] != 0:
                                        grid[row][col]=grid[row][col+3]
                                        grid[row][col+3]=0
                                        grid[row][col+2]=0
                                        grid[row][col+1]=0
    for col in range(0,3):
        for row in range(4):
            if grid[row][col]!=0:
                if grid[row][col]==grid[row][col+1]:
                    grid[row][col]=grid[row][col+1]+grid[row][col]
                    if col==0:
                        grid[row][col+1]=grid[row][col+2]
                        grid[row][col+2]=grid[row][col+3]
                        grid[row][col+3]=0
                    elif col==1:
                        grid[row][col+1]=grid[row][col+2]
                        grid[row][col+2]=0
                    elif col==2:
                        grid[row][col+1]=0
    return grid

def push_right(grid): #same as move up, however column is checked in reverse order, moved right (-) not up (+)
    for col in range(3,-1,-1):
        for row in range(4):
            if grid[row][col]==0:
                if col>0:
                    if grid[row][col-1] != 0:
                        grid[row][col]=grid[row][col-1]
                        grid[row][col-1]=0
                    else: 
                        if col>1:
                            if grid[row][col-2] != 0:
                                grid[row][col]=grid[row][col-2]
                                grid[row][col-2]=0
                                grid[row][col-1]=0
                            else:
                                if col>2:
                                    if grid[row][col-3] != 0:
                                        grid[row][col]=grid[row][col-3]
                                        grid[row][col-3]=0
                                        grid[row][col-2]=0
                                        grid[row][col-1]=0
    for col in range(3,0,-1):
        for row in range(4):
            if grid[row][col]!=0:
                if grid[row][col]==grid[row][col-1]:
                    grid[row][col]=grid[row][col-1]+grid[row][col]
                    if col==3:
                        grid[row][col-1]=grid[row][col-2]
                        grid[row][col-2]=grid[row][col-3]
                        grid[row][col-3]=0
                    elif col==2:
                        grid[row][col-1]=grid[row][col-2]
                        grid[row][col-2]=0
                    elif col==1:
                        grid[row][col-1]=0
    return grid
                    
