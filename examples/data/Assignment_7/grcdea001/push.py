"""program to mimic the movements of game 2048
Dean Gracey
1 May 2014"""

import util

def push_up(grid):

    
    for x in range(0,4):
        
        for y in range(0,3):

            #Move all blocks up
            counter = 1
            while(grid[y][x]==0) and y+counter<4:
                grid[y][x]=grid[y+counter][x]
                grid[y+counter][x]=0
                counter+=1
                
            #blocks that can join get joined
    for x in range (0,4):
        
        for y in range(0,3):
            
            counter2=1
            if(grid[y][x]==grid[y+1][x]):
                grid[y][x]=grid[y][x]*2
                grid[y+1][x]=0
                
    for x in range (0,4):
        for y in range (0,3):
            counter3 = 1
            while(grid[y][x]==0) and y+counter3<4:
                grid[y][x]=grid[y+counter3][x]
                grid[y+counter3][x]=0
                counter3+=1            
            
def push_down(grid):
    push_up(grid)
    
    for x in range(0,4):
        
        for y in range(3,0,-1):
            
            #Move all blocks down
            counter = 1
            while(grid[y][x]==0) and y-counter>=0:
                grid[y][x]=grid[y-counter][x]
                grid[y-counter][x]=0
                counter+=1  

            
def push_left(grid):
    
    for y in range(0,4):
        
        for x in range(0,3):
            #Move all blocks left
            counter = 1
            while(grid[y][x]==0) and x+counter<4:
                grid[y][x]=grid[y][x+counter]
                grid[y][x+counter]=0
                counter+=1            
            #blocks that can join get joined
    for y in range (0,4):
        
        for x in range(0,3):
            
            counter2=1
            if(grid[y][x]==grid[y][x+1]):
                grid[y][x]=grid[y][x]*2
                grid[y][x+1]=0
                    
    for y in range (0,4):
        for x in range (0,3):
            counter3 = 1
            while(grid[y][x]==0) and x+counter3<4:
                grid[y][x]=grid[y][x+counter3]
                grid[y][x+counter3]=0
                counter3+=1                                    

def push_right(grid):
    push_left(grid)
    
    for y in range(0,4):
            
        for x in range(3,0,-1):
            
            #Move all blocks right
            counter = 1
            while(grid[y][x]==0) and x-counter>=0:
                grid[y][x]=grid[y][x-counter]
                grid[y][x-counter]=0
                counter+=1
        