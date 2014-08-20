"""Prmomise Mashinini 
2 may 2014 push , 2048"""
import util
def push_up (grid):
    """merge grid values upwards"""
    grid_copy=[]#grid_copy empty list 
    grid_copy=util.create_grid(grid_copy)
    
    while grid!=grid_copy:
        grid_copy=util.copy_grid(grid)#this calls util and creates a grid copy
        
        for y in range(3):#iterate throught the list in grid 
            for x in range(4):
                if grid[y][x]==0:#if the number is 0 we move the value to the right one unit 
                    grid[y][x]=grid[y+1][x]
                    grid[y+1][x]=0 #zero value is then put in.


    for y in range(3):
        for x in range(4):    
            if grid[y][x]==grid[y+1][x]:
                grid[y][x]= grid[y][x]+grid[y+1][x]
                grid[y+1][x]=0
 
 
 
    for y in range(3):
        for x in range(4):
            if grid[y][x]==0:
                grid[y][x]=grid[y+1][x]
                grid[y+1][x]=0 
    return grid
#            

def push_down (grid):
    """merge grid values downwards"""
 
    grid_copy=[]
    grid_copy=util.create_grid(grid_copy)
    
    while grid!=grid_copy:
        grid_copy=util.copy_grid(grid)
        
        for y in range(3,0,-1):
            for x in range(4):
                if grid[y][x]==0:
                    grid[y][x]=grid[y-1][x]
                    grid[y-1][x]=0

                    
        for x in range(4):    
            if grid[y][x]==grid[y-1][x]:
                grid[y][x]= grid[y][x]+grid[y-1][x]
                grid[y-1][x]=0
    for y in range(3,0,-1):
        for x in range(4):
            if grid[y][x]==0:
                grid[y][x]=grid[y-1][x]
                grid[y-1][x]=0 
    return grid    

def push_left (grid):
    """merge grid values left"""
    grid_copy=[]
    grid_copy=util.create_grid(grid_copy)
      
    while grid!=grid_copy:
        grid_copy=util.copy_grid(grid)
        
        for y in range(4):
            for x in range(3):
                if grid[y][x]==0:
                    grid[y][x]=grid[y][x+1]
                    grid[y][x+1]=0
    for y in range(4):
        for x in range(3):    
            if grid[y][x]==grid[y][x+1]:
                grid[y][x]= grid[y][x]+grid[y][x+1]
                grid[y][x+1]=0
    for y in range(4):
        for x in range(3):
            if grid[y][x]==0:
                grid[y][x]=grid[y][x+1]
                grid[y][x+1]=0 
    return grid        





def push_right (grid):
    """merge grid values right""" 
    grid_copy=[]
    grid_copy=util.create_grid(grid_copy)
      





    while grid!=grid_copy:
        grid_copy=util.copy_grid(grid)
        
        for y in range(4):
            for x in range(3,0,-1):
                if grid[y][x]==0:
                    grid[y][x]=grid[y][x-1]
                    grid[y][x-1]=0
 
 
 
 
    for y in range(4):
        for x in range(3,0,-1):    
            if grid[y][x]==grid[y][x-1]:
                grid[y][x]= grid[y][x]+grid[y][x-1]
                grid[y][x-1]=0





    for y in range(4):
        for x in range(3,0,-1):
            if grid[y][x]==0:
                grid[y][x]=grid[y][x-1]
                grid[y][x-1]=0 
    return grid        