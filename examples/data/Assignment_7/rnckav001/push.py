#ass.7 Q3 2048
#Kavir Ranchod RNCKAV001
#03/05/2014

import util

def push_up(grid):
    """Function to merge grid values upwards."""
    #Temporarily store each comlumns values in a list
    for x in range(4):
        col = []
        for y in range(4):
            col.append(grid[y][x])
        #Remove the "0" in front of certain numbers
            dn = 0
        for num in range(3):
            if col[num-dn] == 0:
                del col[num-dn]
                col.append(0)
                dn += 1
        #Add equal, vertically adjacent values into the top block
        for num in range(3):
            if col[num] == col[num+1]:
                col[num] = col[num]+col[num+1]
                del col[num+1]
                col.append(0)
        #Add each new column back to the grid
        for y in range(4):
            grid[y][x] = col[y]
            
def push_down(grid):
    """Function to merge grid values downwards."""
    #Same code as push_up, but with reverse used to push values down
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