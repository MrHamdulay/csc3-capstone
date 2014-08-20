
#mahdi marcus
#mrcmah001


def push_up (grid):    
    for x in range(4):  #column
        for y in range(3):
            tally=1
            while tally<(4-y) and grid[y][x]==0: 
                grid[y][x]=grid[y+tally][x]
                grid[y+tally][x]=0
                tally+=1
                
    for x in range(4):   #rows
        for y in range(3):
            if grid[y][x] == grid[y+1][x]:
                grid[y][x]=2*grid[y][x]
                grid[y+1][x]=0
            
    for x in range(4):
        for y in range(3):
            tally=1
            while tally<(4-y) and grid[y][x] == 0:
                grid[y][x]=grid[y+tally][x]
                grid[y+tally][x]=0
                tally+=1
            

def push_down (grid):   
    for x in range(4):
        for y in range(3,0,-1):
            tally=1
            while tally<(y+1) and grid[y][x]==0:
                grid[y][x]=grid[y - tally][x]
                grid[y - tally][x]=0
                tally+=1
                
    for x in range(4):
        for y in range(3,0,-1):
            if grid[y][x]==grid[y-1][x]:
                grid[y][x]=2*grid[y][x]
                grid[y-1][x]=0
                
    for x in range(4):
        for y in range(3,0,-1):
            tally=1
            while tally<(y+1) and grid[y][x]==0:
                grid[y][x]=grid[y-tally][x]
                grid[y-tally][x]=0
                tally+=1
                
                
def push_left (grid):    
    for y in range(4):
        for x in range(3):
            tally=1
            while tally<(4-x) and grid[y][x]==0:
                grid[y][x]=grid[y][x+tally]
                grid[y][x+tally]=0
                tally+=1
                
    for y in range(4):
        for x in range(3):
            if grid[y][x]==grid[y][x+1]:
                grid[y][x]=2*grid[y][x]
                grid[y][x+1]=0
                
    for y in range(4):
        for x in range(3):
            tally=1
            while tally<(4-x) and grid[y][x]==0:
                grid[y][x]=grid[y][x+tally]
                grid[y][x+tally]=0
                tally+=1
                

def push_right (grid):     
    for y in range(4):
        for x in range(3,0,-1):
            tally=1
            while tally<(x+1) and grid[y][x]==0:
                grid[y][x]=grid[y][x-tally]
                grid[y][x-tally]=0
                tally+=1
                
    for y in range(4):
        for x in range(3,0,-1):
            if grid[y][x]==grid[y][x-1]:
                grid[y][x]=2*grid[y][x]
                grid[y][x-1]=0
                
    for y in range(4):
        for x in range(3,0,-1):
            tally=1
            while tally<(x+1) and grid[y][x]==0:
                grid[y][x]=grid[y][x-tally]
                grid[y][x-tally]=0
                tally+=1
                
 
