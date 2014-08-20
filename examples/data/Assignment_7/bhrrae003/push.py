"""Raeesa Behardien
BHRRAE003
Assignment 7
Question 3
02 May 2014"""

def push_up (grid):
    """merge grid values upwards"""
    for vertical in range(4): #creates columns
        for horizontal in range(3):
            counting=1
            while counting<(4-horizontal) and grid[horizontal][vertical]==0: 
                grid[horizontal][vertical]=grid[horizontal+counting][vertical]
                grid[horizontal+counting][vertical]=0
                counting+=1
                
    for vertical in range(4): #creates rows
        for horizontal in range(3):
            if grid[horizontal][vertical] == grid[horizontal+1][vertical]:
                grid[horizontal][vertical]=2*grid[horizontal][vertical]
                grid[horizontal+1][vertical]=0
            
    for vertical in range(4):
        for horizontal in range(3):
            counting=1
            while counting<(4-horizontal) and grid[horizontal][vertical] == 0:
                grid[horizontal][vertical]=grid[horizontal+counting][vertical]
                grid[horizontal+counting][vertical]=0
                counting+=1
            

def push_down (grid):
    """merge grid values downwards"""
    for vertical in range(4):
        for horizontal in range(3,0,-1):
            counting=1
            while counting<(horizontal+1) and grid[horizontal][vertical]==0:
                grid[horizontal][vertical]=grid[horizontal - counting][vertical]
                grid[horizontal - counting][vertical]=0
                counting+=1
                
    for vertical in range(4):
        for horizontal in range(3,0,-1):
            if grid[horizontal][vertical]==grid[horizontal-1][vertical]:
                grid[horizontal][vertical]=2*grid[horizontal][vertical]
                grid[horizontal-1][vertical]=0
                
    for vertical in range(4):
        for horizontal in range(3,0,-1):
            counting=1
            while counting<(horizontal+1) and grid[horizontal][vertical]==0:
                grid[horizontal][vertical]=grid[horizontal-counting][vertical]
                grid[horizontal-counting][vertical]=0
                counting+=1
                
                
def push_left (grid):
    """merge grid values left"""
    for horizontal in range(4):
        for vertical in range(3):
            counting=1
            while counting<(4-vertical) and grid[horizontal][vertical]==0:
                grid[horizontal][vertical]=grid[horizontal][vertical+counting]
                grid[horizontal][vertical+counting]=0
                counting+=1
                
    for horizontal in range(4):
        for vertical in range(3):
            if grid[horizontal][vertical]==grid[horizontal][vertical+1]:
                grid[horizontal][vertical]=2*grid[horizontal][vertical]
                grid[horizontal][vertical+1]=0
                
    for horizontal in range(4):
        for vertical in range(3):
            counting=1
            while counting<(4-vertical) and grid[horizontal][vertical]==0:
                grid[horizontal][vertical]=grid[horizontal][vertical+counting]
                grid[horizontal][vertical+counting]=0
                counting+=1
                

def push_right (grid):
    """merge grid values right""" 
    for horizontal in range(4):
        for vertical in range(3,0,-1):
            counting=1
            while counting<(vertical+1) and grid[horizontal][vertical]==0:
                grid[horizontal][vertical]=grid[horizontal][vertical-counting]
                grid[horizontal][vertical-counting]=0
                counting+=1
                
    for horizontal in range(4):
        for vertical in range(3,0,-1):
            if grid[horizontal][vertical]==grid[horizontal][vertical-1]:
                grid[horizontal][vertical]=2*grid[horizontal][vertical]
                grid[horizontal][vertical-1]=0
                
    for horizontal in range(4):
        for vertical in range(3,0,-1):
            counting=1
            while counting<(vertical+1) and grid[horizontal][vertical]==0:
                grid[horizontal][vertical]=grid[horizontal][vertical-counting]
                grid[horizontal][vertical-counting]=0
                counting+=1
                

