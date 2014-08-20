
"""To create a code for the 2048 game
Tsanwani Vhonani
30 April 2014"""

import util
def push(l):
    for row in range(l.count(0)):
        col=0
        while col<3:
            if l[col]==0:
                l[col]=l[col+1]
                l[col+1]-=l[col+1]
            col+=1
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
    #merge grid values upwards
    for row in range(4):
        column=[]
        for col in range(4):
            column.append(grid[col][row])      
        push(column)
        add(column)
        push(column)

        for i in range(4):
            grid[i][row] = column[i]
          
            
def push_down (grid):
    #merge grid values downwards    
    for row in range(4):
        column = []
        for col in range(3,-1,-1):
            column.append(grid[col][row])
        push(column)
        add(column)
        push(column)
        x=0
        for i in range(3,-1,-1):
            grid[i][row] = column[x]
            x+=1
    
    
    
def push_left (grid):
    #merge grid values left
    for row in range(4):
        rows = []
        for col in range(4):
            rows.append(grid[row][col])
        push(rows)
        add(rows)
        push(rows)        
        
        for i in range(4):
            grid[row][i] = rows[i]

def push_right (grid):
    #merge grid values right 
    for row in range(4):
        rows = []
        for col in range(3,-1,-1):
            rows.append(grid[row][col])
        push(rows)
        add(rows)
        push(rows)
        m=0
        for i in range(3,-1,-1):
            grid[row][i] = rows[m]
            m+=1
                    
    
    