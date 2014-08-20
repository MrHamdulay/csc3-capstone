'''
Created on 02 May 2014
2048 movements
@author: Yusuf Khan
KHNYUS005
'''
def push_up (grid):
    """merge grid values upwards"""
    for c in range(3,0,-1):
        for i in range(4):#nested loop iterates through grid
            if grid[c][i]==grid[c-1][i]:
                grid[c][i]=0#if adjacent equal, add
                grid[c-1][i]=(2*int(grid[c-1][i]))
                if c!=3:
                    grid[c][i]=grid[c+1][i]
                    grid[c+1][i]=0#if values are added, move value to old position
            if grid[c-1][i]==0:#if block empty shift from adjacent block
                grid[c-1][i]=grid[c][i]
                grid[c][i]=0
                if c!=3:
                    grid[c][i]=grid[c+1][i]
                    grid[c+1][i]=0#if values are added, move value to old position

def push_down (grid):
    """merge grid values downwards"""
    for c in range(3):
        for i in range(4):#nested loop iterates through grid
            if grid[c][i]==grid[c+1][i]:
                grid[c][i]=0#if adjacent equal, add
                grid[c+1][i]=(2*grid[c+1][i])
                if c!=0:
                    grid[c][i]=grid[c-1][i]
                    grid[c][i-1]=0#if values are added, move value to old position
            if grid[c+1][i]==0:#if block empty shift from adjacent block
                grid[c+1][i]=grid[c][i]
                grid[c][i]=0  
                if i!=0:
                    grid[c][i]=grid[c][i-1]
                    grid[c][i-1]=0#if values are added, move value to old position 

def push_right (grid):
    """merge grid values left"""
    for c in range (4):
        for i in range (3):#nested loop iterates through grid
            if grid[c][i]==grid[c][i+1]:
                grid[c][i]=0#if adjacent equal, add
                grid[c][i+1]=(2*int(grid[c][i+1]))
                if i!=0:
                    grid[c][i]=grid[c][i-1]
                    grid[c][i-1]=0#if values are added, move value to old position
            if grid[c][i+1]==0:#if block empty shift from adjacent block
                grid[c][i+1]=grid[c][i]
                grid[c][i]=0
                if i!=0:
                    grid[c][i]=grid[c][i-1]
                    grid[c][i-1]=0#if values are added, move value to old position           

def push_left (grid):
    """merge grid values right"""
    for c in range (4):  
        for i in range (3,0,-1):#nested loop iterates through grid
            if grid[c][i]==grid[c][i-1]:
                grid[c][i]=0#if adjacent equal, add
                grid[c][i-1]=(2*int(grid[c][i-1]))
                if i!=3:#if values are added, move value to old position
                    grid[c][i]=grid[c][i+1]
                    grid[c][i+1]=0
            if grid[c][i-1]==0:#if block empty shift from adjacent block
                grid[c][i-1]=grid[c][i] 
                grid[c][i]=0 
                if i!=3:
                    grid[c][i]=grid[c][i+1]
                    grid[c][i+1]=0#if values are added, move value to old position      