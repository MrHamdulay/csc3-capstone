#Programme writing functions for 2048 game
#Joe Sutton
#30 April 2014

import util

def push_up (grid):
    """merge grid values upwards"""
    
    for collumn in range(4):
            newcollumn=[]
            for row in range(4):
                newvalue=grid[row][collumn]
                newcollumn.append(newvalue)
                
            while 0 in newcollumn:
                newcollumn.remove(0)
                
            i=0
                
            while i<(len(newcollumn)-1):
                if newcollumn[i]==newcollumn[i+1]:
                    newcollumn[i]=newcollumn[i]*2
                    del newcollumn[i+1]
                    i+=1
                else:
                    i+=1
            for i in range(4-len(newcollumn)):
                newcollumn.append(0)
                
            for i in range(4):
                grid[i][collumn]=newcollumn[i]    
        

def push_down (grid):
    """merge grid values downwards"""

    grid.reverse()
    
    push_up(grid)
    
    grid.reverse()
            
def push_left (grid):
    """merge grid values left"""
    row=0
    while row<4:
        collumnvalue=0
        collumn=0
        while collumnvalue<4:
            if grid[row][collumn]==0:
                del grid[row][collumn]
                collumnvalue+=1
            else:
                collumn+=1
                collumnvalue+=1
        row+=1
    
    for row in grid:
        i=0
        while i <(len(row)-1):
            if row[i]==row[i+1]:
                row[i]=row[i]*2
                del row[i+1]
                i+=1
            else: i+=1
                
    
    for row in grid:
        lengthofrow=len(row)
        for i in range(4-lengthofrow):
            row.append(0)

def push_right (grid):
    """merge grid values right"""
    newgrid=[]
    for row in grid:
        newrow=row.reverse()
        newgrid.append(newrow)
    
    reversegrid=push_left (grid)
    for row in grid:
        row=row.reverse()
        