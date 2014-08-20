'''A program that is the set of merging functions that merge adjacent equal values and eliminate gaps
Daniel M. Tamale
TMLDAN001
2014-04-27'''

def push_up (grid):
    """merge grid values upwards"""
    for n in range (4):
        for col in range(3,0,-1):
            for i in range(4):
                if grid[col-1][i]==0:
                    grid[col-1][i]=grid[col][i]
                    grid[col][i]=0
                    
    for col in range(3):
        for i in range(4):
            if grid[col+1][i]==grid[col][i]:
                grid[col][i]*=2
                grid[col+1][i]=0
    
    for n in range(4):
        for col in range(3,0,-1):
            for i in range(4):
                if grid[col-1][i]==0:
                    grid[col-1][i]=grid[col][i]
                    grid[col][i]=0        
                    
def push_down (grid):
    """merge grid values downwards"""
    for n in range (4):
        for col in range(3):
            for i in range(4):
                if grid[col+1][i]==0:
                    grid[col+1][i]=grid[col][i]
                    grid[col][i]=0
                               
    for col in range(3,0,-1):
        for i in range(4):
            if grid[col-1][i]==grid[col][i]:
                grid[col][i]*=2
                grid[col-1][i]=0
               
    for n in range(4):
        for col in range(3):
            for i in range(4):
                if grid[col+1][i]==0:
                    grid[col+1][i]=grid[col][i]
                    grid[col][i]=0            
       
def push_left (grid):
    """merge grid values left"""
    for n in range (4):
        for row in range(3,0,-1):
            for i in range(4):
                if grid[i][row-1]==0:
                    grid[i][row-1]=grid[i][row]
                    grid[i][row]=0
                               
    for row in range(3):
        for i in range(4):
            if grid[i][row+1]==grid[i][row]:
                grid[i][row]*=2
                grid[i][row+1]=0
               
    for n in range(4):
        for row in range(3,0,-1):
            for i in range(4):
                if grid[i][row-1]==0:
                    grid[i][row-1]=grid[i][row]
                    grid[i][row]=0          
       
def push_right (grid):
    """merge grid values right"""
    for n in range (3):
        for row in range(3):
            for i in range(4):
                if grid[i][row+1]==0:
                    grid[i][row+1]=grid[i][row]
                    grid[i][row]=0
                                   
    for row in range(4):
        for i in range(3,0,-1):
            if grid[i][row-1]==grid[i][row]:
                grid[i][row]*=2
                grid[i][row-1]=0
                   
    for n in range(3):
        for row in range(3):
            for i in range(4):
                if grid[i][row+1]==0:
                    grid[i][row+1]=grid[i][row]
                    grid[i][row]=0          
