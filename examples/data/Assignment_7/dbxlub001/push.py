"""Lubalethu Dube
April 2 2014
my first game!! :)"""
grid = [[2,0,2,0],[0,4,0,8],[0,16,0,4],[2,2,2,2]]
import copy
def push_up (grid):
    """merge grid values upwards"""
    v=0
    #run through all spaces
    for k in range(3):
        for i in range(1,4):
            for j in range(4):
                if grid[i-1][j]==0 or grid[i-1][j]==" " or grid[i-1][j]=="":
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=v
    #check if top guys are equal then add them
    for i in range (1,4):
        for j in range(4):
            if grid[i-1][j]==grid[i][j]:
                grid[i-1][j]+=grid[i][j]
                grid[i][j]=v
    
    #fill in the blanks
    for i in range (1,4):
        for j in range(4):
            if grid[i-1][j]==" " or grid[i-1][j]==0:
                grid[i-1][j]=grid[i][j]
                grid[i][j]=v
    return grid
                
def push_down (grid):
    #turn grid around
    grid.reverse()
    #push up
    new_gridy=push_up (grid)
    #change it bak to the right side up
    new_gridy.reverse()
    return new_gridy

def push_left (grid):
    """merge grid values left"""
    
    v=0
    #run through all spaces
    for k in range(3):
        for i in range(4):
            for j in range(1,4):
                
                if grid[i][j-1]==0 or grid[i][j-1]==" " or grid[i][j-1]=="": 
                    grid[i][j-1]=grid[i][j]
                    grid[i][j]=v
    #check if top guys are equal then add them
    for i in range (4):
        for j in range(1,4):
            if grid[i][j-1]==grid[i][j]:
                grid[i][j-1]+=grid[i][j]
                grid[i][j]=v
    
    #fill in the blanks
    for i in range (4):
        for j in range(1,4):
            if grid[i][j-1]==" " or grid[i][j-1]==0 or grid[i][j-1]=="" :
                grid[i][j-1]=grid[i][j]
                grid[i][j]=v
    return grid    

def push_right (grid):
    """merge grid values right"""
    
    #Use push up function
    gridy=copy.deepcopy(grid)
    #turn it around...
    for i in range(4):
        grid[i][0]=gridy[i][3]
        grid[i][1]=gridy[i][2]
        grid[i][2]=gridy[i][1]
        grid[i][3]=gridy[i][0]
    
    #use push function
    gridy2= push_left(grid)
    gridy3=copy.deepcopy(gridy2)
    #then back around
    for i in range(4):
        grid[i][0]=gridy3[i][3]
        grid[i][1]=gridy3[i][2]
        grid[i][2]=gridy3[i][1]
        grid[i][3]=gridy3[i][0]
    return grid
    
        
    