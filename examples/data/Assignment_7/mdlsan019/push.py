'''Sanele Mdlalose
   MDLSAN019
   02-April-2014
   2048'''

def push_up (grid):
    for i in range (4):
        for row in range (1,4):
            for col in range (4):
                
                    
                if grid[row][col]==grid[row-1][col]:
                    grid[row-1][col]=(grid[row][col])*2
                    grid[row][col]=0
                elif grid[row-1][col]==0:
                    grid[row-1][col]=grid[row][col]
                    grid[row][col]=0
                else:             
                    grid[row][col]=grid[row][col]
def push_down (grid):   
    for i in range (4):
        for row in range (2,-1,-1):
            for col in range (4):
            
            
                    
                if grid[row][col]==grid[row+1][col]:
                    grid[row+1][col]=(grid[row][col])*2
                    grid[row][col]=0
                elif grid[row+1][col]==0:
                    grid[row+1][col]=grid[row][col]
                    grid[row][col]=0
                else:
                    grid[row][col]=grid[row][col]
                    
def push_left (grid):
    for i in range (4):
        for row in range (4):
            for col in range (3,0,-1):
                
                
                if grid[row][col]==grid[row][col-1]:
                    grid[row][col-1]=(grid[row][col-1])+(grid[row][col])
                    grid[row][col]=0
                elif grid[row][col-1]==0:
                    grid[row][col-1]=grid[row][col]
                    grid[row][col]=0
               
                        


def push_right (grid):
    for i in range (4):
        for row in range (4):
            for col in range (0,3):
                if grid[row][col]==grid[row][col+1]:
                    grid[row][col+1]=(grid[row][col])*2
                    grid[row][col]=0
                elif grid[row][col+1]==0:
                    grid[row][col+1]=grid[row][col]
                    grid[row][col]=0