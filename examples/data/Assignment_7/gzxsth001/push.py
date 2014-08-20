
"""To create a code for the 2048 game
Sthabiso Andile Gazu
 may 2014"""

import util
def push(l):
    for i in range(l.count(0)):
        j=0
        while j<3:
            if l[j]==0:
                l[j]=l[j+1]
                l[j+1]-=l[j+1]
            j+=1
    return l
def add(l):
    i = 0
    while i < 3:
        if l[i] == l[i+1]:
            l[i] *= 2
            l[i+1] *= 0
        i += 1
    return l
    
def push_up (grid):
    """merge grid values upwards"""
    for c in range(4):
        column=[]
        for r in range(4):
            column.append(grid[r][c])      
        push(column)
        add(column)
        push(column)

        for i in range(4):
            grid[i][c] = column[i]
          
            
   

def push_down (grid):
    """merge grid values downwards"""    
    for c in range(4):
        column = []
        for r in range(3,-1,-1):
            column.append(grid[r][c])
        push(column)
        add(column)
        push(column)
        j=0
        for i in range(3,-1,-1):
            grid[i][c] = column[j]
            j+=1
    
    
    
def push_left (grid):
    """merge grid values left"""
    for r in range(4):
        rows = []
        for c in range(4):
            rows.append(grid[r][c])
        push(rows)
        add(rows)
        push(rows)        
        
        for i in range(4):
            grid[r][i] = rows[i]

def push_right (grid):
    """merge grid values right""" 
    for r in range(4):
        rows = []
        for c in range(3,-1,-1):
            rows.append(grid[r][c])
        push(rows)
        add(rows)
        push(rows)
        j=0
        for i in range(3,-1,-1):
            grid[r][i] = rows[j]
            j+=1
                    
    
    