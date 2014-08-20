"""Module to move merge grid values in a specified direction.
Kemeshan Naicker
5 May 2014"""

import util


            
def push_down(grid):
    """Function to merge grid values downwards."""
    #Follows the same code as function "push_up(grid)" but uses the list reverse function such that zeroes are
    #deleted and blocks added from bottom to top.
    for x in range(4):
        col = []
        for y in range(4):
            col.append(grid[y][x])
            dn = 0
        col.reverse()
        for num in range(3):
            if col[num-dn] == 0:
                del col[num-dn]
                col.append(0)
                dn += 1
        for num in range(3):
            if col[num] == col[num+1]:
                col[num] = col[num]+col[num+1]
                del col[num+1]
                col.append(0)
        col.reverse()
        for y in range(4):
            grid[y][x] = col[y]

def push_up(grid):
    """Function to merge grid values upwards."""
    #Find the grid values from each column and store each as col
    for x in range(4):
        col = []
        for y in range(4):
            col.append(grid[y][x])
    #Delete the zeroes preceding significant numbers. "dn" counts which allows for
            #the deletion of successive zeroes.
            dn = 0
        for num in range(3):
            if col[num-dn] == 0:
                del col[num-dn]
                col.append(0)
                dn += 1
            #Going from top to bottom in the original grid, add equal adjacent numbers and store the sum in the
            #upper of the two blocks.
        for num in range(3):
            if col[num] == col[num+1]:
                col[num] = col[num]+col[num+1]
                del col[num+1]
                col.append(0)
            #Transcribe each new column onto the original grid.
        for y in range(4):
            grid[y][x] = col[y]

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
            
