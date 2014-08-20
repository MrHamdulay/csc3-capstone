"""program to move merge grid values in a specified direction
thushar hariparsad
5 may 2014"""

import util

def push_up(grid): #push grid up
    #Extract the grid values from each column and temporarily store each as "col."
    for x in range(4):
        col = []
        for y in range(4):
            col.append(grid[y][x])
        """Remove all zeroes preceding significant numbers. Variable "dn" is an accumulator which allows for
        the deletion of successive zeroes."""
        dn = 0
        for n in range(3):
            if col[n-dn] == 0:
                del col[n-dn]
                col.append(0)
                dn += 1
        """Going from top to bottom in the original grid, add equal adjacent numbers and store the sum in the
        upper of the two blocks."""
        for num in range(3):
            if col[n] == col[n+1]:
                col[n] = col[n]+col[n+1]
                del col[n+1]
                col.append(0)
        for y in range(4):
            grid[y][x] = col[y]
            
def push_down(grid):
    #move grid down
    for x in range(4):
        col = []
        for y in range(4):
            col.append(grid[y][x])
            dn = 0
        col.reverse()
        for n in range(3):
            if col[n-dn] == 0:
                del col[n-dn]
                col.append(0)
                dn += 1
        for n in range(3):
            if col[n] == col[n+1]:
                col[n] = col[n]+col[n+1]
                del col[n+1]
                col.append(0)
        col.reverse()
        for y in range(4):
            grid[y][x] = col[y]

def push_left(grid):
    #Move grid left
    for y in range(4):
        row = []
        for x in range(4):
            row.append(grid[y][x])
            dn = 0
        for n in range(3):
            if row[n-dn] == 0:
                del row[n-dn]
                row.append(0)
                dn += 1
        for n in range(3):
            if row[n] == row[n+1]:
                row[n] = row[n]+row[n+1]
                del row[n+1]
                row.append(0)
        for x in range(4):
            grid[y][x] = row[x]
            
def push_right(grid):
   #move grid right
    for y in range(4):
        row = []
        for x in range(4):
            row.append(grid[y][x])
            dn = 0
        row.reverse()
        for n in range(3):
            if row[n-dn] == 0:
                del row[n-dn]
                row.append(0)
                dn += 1
        for n in range(3):
            if row[n] == row[n+1]:
                row[n] = row[n]+row[n+1]
                del row[n+1]
                row.append(0)
        row.reverse()
        for x in range(4):
            grid[y][x] = row[x]            
            
