"""More functions than I need: 2048 game
Christopher Sterley
27/04/2014"""

import util

def push_up (grid):
    """merge grid values upwards"""
    
    #moves values up
    for row in range(3):
        for column in range(4):
                if grid[row][column]==0:
                    grid[row][column]=grid[row+1][column]
                    grid[row+1][column]=0
                    
    #moves values up
    for row in range(3):
        for column in range(4):
                if grid[row][column]==0:
                    grid[row][column]=grid[row+1][column]
                    grid[row+1][column]=0    
    
    #checks for similar values and combines
    for row in range(3):
        for column in range(4):
                if grid[row][column]==grid[row+1][column]: 
                    grid[row][column]=2*grid[row][column]
                    grid[row+1][column]=0
                
    #moves remaining values up            
    for row in range(3):
        for column in range(4):
                if grid[row][column]==0: 
                    grid[row][column]=grid[row+1][column]
                    grid[row+1][column]=0
                

def push_down (grid):
    """merge grid values downwards"""
    
    #moves values down
    for row in range (3,0,-1):
        for column in range (4):
            if grid[row][column]==0 and grid[row-1][column]!=0:
                grid[row][column]=grid[row-1][column]
                grid[row-1][column]=0
                
    #moves values down
    for row in range (3,0,-1):
        for column in range (4):
            if grid[row][column]==0 and grid[row-1][column]!=0:
                grid[row][column]=grid[row-1][column]
                grid[row-1][column]=0    
   
   #checks for similar values and combines whilst ensuring values dont get added twice
    check_row=-1
    check_column=-1
    for row in range (0,3):
        for column in range (4):
            #check if values have been added already
            if row==check_row and column==check_column:
                continue
            
            elif grid[row][column]==grid[row+1][column]:
                grid[row+1][column]= 2*grid[row][column]
                grid[row][column]=0
                check_row=row+1
                check_column=column
                
            elif grid[row+1][column] == 0:
                grid[row+1][column]=grid[row][column]
                grid[row][column]=0
         
              
    for row in range (3,0,-1):
        for column in range (4):
            if grid[row][column]==0 and grid[row-1][column]!=0:
                grid[row][column]=grid[row-1][column]
                grid[row-1][column]=0  
    
    for row in range (3,0,-1):
        for column in range (4):
            if grid[row][column]==0 and grid[row-1][column]!=0:
                grid[row][column]=grid[row-1][column]
                grid[row-1][column]=0                

def push_left (grid):
    """merge grid values left"""
    
    #moves values left
    for row in range(4):
        for column in range(3):
                if grid[row][column]==0:
                    grid[row][column]=grid[row][column+1]
                    grid[row][column+1]=0
                    
                    
    #moves values left
    for row in range(4):
        for column in range(3):
                if grid[row][column]==0:
                    grid[row][column]=grid[row][column+1]
                    grid[row][column+1]=0    
                
    
    #checks for similar values and combines
    for row in range(4):
        for column in range(3):
                if grid[row][column]==grid[row][column+1]:
                    grid[row][column]=2*grid[row][column]
                    grid[row][column+1]=0
                    
    #moves remaining values left                
    for row in range(4):
        for column in range(3):
                if grid[row][column]==0:
                    grid[row][column]=grid[row][column+1]
                    grid[row][column+1]=0               
    

def push_right (grid):
    """merge grid values right"""
    
    #moves values right
    for row in range(4):
        for column in range(3,0,-1):
                    if grid[row][column]==0:
                        grid[row][column]=grid[row][column-1]
                        grid[row][column-1]=0
                        
                        
    #moves values right
    for row in range(4):
        for column in range(3,0,-1):
                    if grid[row][column]==0:
                        grid[row][column]=grid[row][column-1]
                        grid[row][column-1]=0    
                    
    
    #checks for similar values and combine
    for row in range(4):
        for column in range(2,-1,-1):
                    if grid[row][column]==grid[row][column+1]:
                        grid[row][column+1]=2*grid[row][column+1]
                        grid[row][column]=0
                        
    
    #moves remaining values right                    
    for row in range(4):
        for column in range(3,0,-1):
                    if grid[row][column]==0:
                        grid[row][column]=grid[row][column-1]
                        grid[row][column-1]=0
                          
    