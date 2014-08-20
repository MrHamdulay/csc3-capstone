#Phumelele Ndimande
#Assignment 7

import util

def push_up(grid):
    """Function to merge grid values upwards."""
    #Extract the grid values from each column and temporarily store each as "column."
    for x in range(4):
        column = []
        for y in range(4):
            column.append(grid[y][x])
        
            dn = 0
        for num in range(3):
            if column[num-dn] == 0:
                del column[num-dn]
                column.append(0)
                dn += 1
        
        for num in range(3):
            if column[num] == column[num+1]:
                column[num] = column[num]+column[num+1]
                del column[num+1]
                column.append(0)
        #Transcribe each new column onto the original grid.
        for y in range(4):
            grid[y][x] = column[y]
            
def push_down(grid):
    """Function to merge grid values downwards."""
    #zeroes are deleted and blocks added using list reverse function
    
    for x in range(4):
        column = []
        for y in range(4):
            column.append(grid[y][x])
            dn = 0
        column.reverse()
        for num in range(3):
            if column[num-dn] == 0:
                del column[num-dn]
                column.append(0)
                dn += 1
        for num in range(3):
            if column[num] == column[num+1]:
                column[num] = column[num]+column[num+1]
                del column[num+1]
                column.append(0)
        column.reverse()
        for y in range(4):
            grid[y][x] = column[y]

def push_left(grid):
    """Function to merge grid values left."""
    for y in range(4):
        row = []
        for x in range(4):
            row.append(grid[y][x])
            dn = 0
        for num in range(3):
            if row[num-dn] == 0:
                del row[num-dn]
                row.append(0)
                dn += 1
        for num in range(3):
            if row[num] == row[num+1]:
                row[num] = row[num]+row[num+1]
                del row[num+1]
                row.append(0)
        for x in range(4):
            grid[y][x] = row[x]
            
def push_right(grid):
    """Function to merge grid values right."""
    for y in range(4):
        row = []
        for x in range(4):
            row.append(grid[y][x])
            dn = 0
        row.reverse()
        for num in range(3):
            if row[num-dn] == 0:
                del row[num-dn]
                row.append(0)
                dn += 1
        for num in range(3):
            if row[num] == row[num+1]:
                row[num] = row[num]+row[num+1]
                del row[num+1]
                row.append(0)
        row.reverse()
        for x in range(4):
            grid[y][x] = row[x]            
            
