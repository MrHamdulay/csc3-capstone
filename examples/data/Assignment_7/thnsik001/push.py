"""Sikhulile Thenjwayo
Assignment 7 q3
01/05/2014"""

import util
def push_up(grid):
    #merge grid values upwards
    copy = [0,0,0,0]   
    for col in range (4):  
        #1d array of column
        for row in range (4):
            copy[row] = grid[row][col]
        copy = deleteup(copy)
        add(copy)
        copy = deleteup(copy)
        for row in range (4):
            grid[row][col]  = copy[row]  
            
def push_down(grid):
    #merge grid values down
    copy = [0,0,0,0]
    for col in range (4):  
        #1d array of column
        for row in range (4):
            copy[row] = grid[row][col]
        copy = deletedown(copy)
        add(copy)
        copy = deletedown(copy)
        for row in range (4):
            grid[row][col]  = copy[row]                 
            
def deleteup(copy):
    count =0
    while count < len(copy):
        if copy[count] == 0:
            del copy[count]
            count-=1
        count +=1         
    for y in range(4-len(copy)):
        copy.append(0)
    return copy
        
def deletedown(copy):
    count =0
    while count < len(copy):
        if copy[count] == 0:
            del copy[count]
            count-=1
        count +=1    
    for y in range(4-len(copy)):
        copy.insert(y,0)     
    return copy

def add(copy):
    for z in range(3):
        if copy[z] == copy[z+1]:
            copy[z] *= 2
            copy[z+1]=0 
    else:
        if copy[3] == copy[2]:
            copy[3] *= 2
            copy[2]=0             
            
def push_left(grid):
    #merge grid values left
    for row in range (4):
        copy = [0,0,0,0]   
        for col in range (4):
            copy[col] = grid[row][col]
        copy = deleteup(copy)
        add(copy)
        copy = deleteup(copy)
        for col in range (4):
            grid[row][col]  = copy[col] 
            
def push_right(grid):
    #merge grid values rigth
    for row in range (4):
        copy = [0,0,0,0]   
        for col in range (4):
            copy[col] = grid[row][col]
        copy = deletedown(copy)
        add(copy)
        copy = deletedown(copy)
        for col in range (4):
            grid[row][col]  = copy[col]     