"""functions to merge adjacent numbers
Jacqueline Blomendahl
30 April 2014"""

import util

def push_up (grid):
    """merge grid values upwards"""
    for i in range(4):
        for k in range(4):
            if grid[i][k]==0:
                continue
            if i!=0:
                if grid[i][k]==grid[i-1][k]:
                    grid[i-1][k]==grid[i-1][k] + grid[i][k]
                    grid[i][k]==0
                if grid[i-1][k]==0:
                    grid[i-1][k]==grid[i][k]
                if grid[i][k]!=grid[i-1][k]:
                    continue
            if i==0:
                if grid[i][k]==0:
                    grid[i][k]==grid[i-1][k]
                else:
                    continue    
            

def push_down (grid):
    """merge grid values downwards"""
    for i in range(4):
        for k in range(4):
            if grid[i][k]==0:
                continue
            if i!=3:
                if grid[i][k]==grid[i+1][k]:
                    grid[i+1][k]==grid[i+1][k] + grid[i][k]
                    grid[i][k]==0
                if grid[i+1][k]==0:
                    grid[i+1][k]==grid[i][k]
                if grid[i][k]!=grid[i+1][k]:
                    continue
            if i==3:
                if grid[i][k]==0:
                    grid[i][k]==grid[i+1][k]
                else:
                    continue    

def push_left (grid):
    """merge grid values left"""
    for i in range(4):
        for k in range(4):
            if grid[i][k]==0:
                continue
            if k!=0:
                if grid[i][k]==grid[i][k-1]:
                    grid[i][k-1]==grid[i][k-1] + grid[i][k]
                    grid[i][k]==0
                if grid[i][k-1]==0:
                    grid[i][k-1]==grid[i][k]
                if grid[i][k]!=grid[i][k-1]:
                    continue
            if k==0:
                if grid[i][k]==0:
                    grid[i][k]==grid[i][k+1]
                else:
                    continue

def push_right (grid):
    """merge grid values right""" 
    for i in range(4):
            for k in range(4):
                if grid[i][k]==0:
                    continue
                if k!=3:
                    if grid[i][k]==grid[i][k+1]:
                        grid[i][k+1]==grid[i][k+1] + grid[i][k]
                        grid[i][k]==0
                    if grid[i][k+1]==0:
                        grid[i][k+1]==grid[i][k]
                    if grid[i][k]!=grid[i][k+1]:
                        continue
                if k==3:
                    if grid[i][k]==0:
                        grid[i][k]==grid[i][k-1]
                    else:
                        continue
                
                    
              