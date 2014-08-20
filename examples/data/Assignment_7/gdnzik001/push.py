"""Program to write functions to repeatedlymerge adjacent numbers in a grid
Zikho Godana
01 May 2014"""

height=4

def push_up(grid):
    """merge grid values upwards"""
    
    for row in range(height):
        for col  in range(height):
            if row>0:
                if grid[row][col]!=0:
                    if grid[0][col]==0 and grid[1][col]!=0:
                        grid[0][col]=grid[1][col]
                        grid[1][col]=grid[2][col]
                        grid[2][col]=grid[3][col]
                        grid[3][col]=0
                    elif grid[0][col]==0 or grid[0][col]==grid[row][col]:
                        grid[0][col]=grid[0][col]+grid[row][col]
                        grid[row][col]=0
                    elif grid[row][col]!=grid[0][col] and grid[1][col]==0:
                        grid[1][col]=grid[row][col]
                        grid[row][col]=0
                    elif grid[row][col]==grid[row-1][col]:
                        grid[row-1][col]=grid[row][col]+grid[row-1][col]
                        grid[row][col]=0
                    elif grid[row-1][col]==0 and grid[row-2][col]==grid[row][col]:
                        grid[row-2][col]=grid[row][col]+grid[row-2][col]
                        grid[row][col]=0
                    elif grid[row][col]==32:
                        return
            
           
                
                
def push_down(grid):
    """merge grid values downwards"""
    for row in range(height):
        for col in range(height):
            if row<3:
                if grid[row][col]!=0:
                    if grid[3][col]==0 and grid[2][col]!=0:
                        grid[3][col]=grid[2][col]
                        grid[2][col]=grid[1][col]
                        grid[1][col]=grid[0][col]
                        grid[0][col]=0
                    if grid[3][col]==0 or grid[3][col]==grid[row][col]:
                        grid[3][col]=grid[3][col]+grid[row][col]
                        grid[row][col]=0
                    elif grid[3][col]!=grid[row][col] and grid[2][col]==0:
                        grid[2][col]=grid[row][col]
                        grid[row][col]=0
                    elif grid[row][col]==grid[row+1][col]:
                        grid[row+1][col]=grid[row][col]+grid[row+1][col]
                        grid[row][col]=0
                    elif grid[row+1][col]==0:
                        grid[row+1][col]=grid[row][col]
                        grid[row][col]=0 
                    elif grid[row][col]==32:
                        return                        
                    
def push_left(grid):
    """merge grid values left"""
    for row in range(height):
        for col in range(height):
            if col>0:
                if grid[row][col]!=0:
                    if grid[row][0]==0 and grid[row][1]!=0:
                        grid[row][0]=grid[row][1]
                        grid[row][1]=grid[row][2]
                        grid[row][2]=grid[row][3]
                        grid[row][3]=0
                    elif grid[row][0]==0 or grid[row][col]==grid[row][0]:
                        grid[row][0]=grid[row][0]+grid[row][col]
                        grid[row][col]=0
                    elif grid[row][0]!=grid[row][col] and grid[row][1]==0:
                        grid[row][1]=grid[row][col]
                        grid[row][col]=0
                    elif grid[row][col-1]==0 and grid[row][col-2]==grid[row][col]:
                        grid[row][col-2]=grid[row][col]+grid[row][col-2]
                        grid[row][col]=0
                    elif grid[row][col]==grid[row][col-1]:
                        grid[row][col-1]=grid[row][col]+grid[row][col-1]
                        grid[row][col]=0
                    elif grid[row][col]==32:
                        return                    
                    
def push_right(grid):
    """merge grid values right"""
    for row in range(height):
        for col in range(height):
            if col<3:
                if grid[row][col]!=0:
                    if grid[row][3]==0 and grid[row][2]!=0:
                        grid[row][3]=grid[row][2]
                        grid[row][2]=grid[row][1]
                        grid[row][1]=grid[row][0]
                        grid[row][0]=0
                    elif grid[row][3]==0 or grid[row][col]==grid[row][3]:
                        grid[row][3]=grid[row][3]+grid[row][col]
                        grid[row][col]=0
                    elif grid[row][3]!=grid[row][col] and grid[row][2]==0:
                        grid[row][2]=grid[row][col]
                        grid[row][col]=0
                    elif grid[row][col+1]==0:
                        grid[row][col+1]=grid[row][col]
                        grid[row][col]=0
                    elif grid[row][col]==grid[row][col+1]:
                        grid[row][col+1]=grid[row][col]+grid[row][col+1]
                        grid[row][col]=0 
                    elif grid[row][col]==32:
                        return                    