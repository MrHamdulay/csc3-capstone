'''
Created on 02 May 2014
2048 movements
@author: Yusuf Khan
KHNYUS005
'''
def push_up(grid):
    """Function to merge grid values upwards."""
    for x in range(4):
        down = []
        for y in range(4):
            down.append(grid[y][x])#creates list of values in column
            ac = 0
            
        for num in range(3):
            if down[num-ac] == 0:
                del down[num-ac]
                down.append(0)
                ac += 1
        #remove zeroes and add equal adjacent numbers
        
        for num in range(3):
            if down[num] == down[num+1]:
                down[num] = down[num]+down[num+1]
                del down[num+1]
                down.append(0)
                
        #Return column to grid
        for y in range(4):
            grid[y][x] = down[y]
            
def push_down(grid):
    """Function to merge grid values downwards."""
    for x in range(4):
        down = []
        for y in range(4):
            down.append(grid[y][x])#extracts column
            ac = 0
            
        down.reverse()#reversed to add values in correct order
        for num in range(3):#the rest of the program uses the same technique
            if down[num-ac] == 0:
                del down[num-ac]
                down.append(0)
                ac += 1
                
        for num in range(3):
            if down[num] == down[num+1]:
                down[num] = down[num]+down[num+1]
                del down[num+1]
                down.append(0)
                
        down.reverse()
        for y in range(4):
            grid[y][x] = down[y]

def push_left(grid):
    """Function to merge grid values left."""
    for y in range(4):
        row = []
        for x in range(4):
            row.append(grid[y][x])
            ac = 0
            
        for num in range(3):
            if row[num-ac] == 0:
                del row[num-ac]
                row.append(0)
                ac += 1
                
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
            ac = 0
            
        row.reverse()
        for num in range(3):
            if row[num-ac] == 0:
                del row[num-ac]
                row.append(0)
                ac += 1
                
        for num in range(3):
            if row[num] == row[num+1]:
                row[num] = row[num]+row[num+1]
                del row[num+1]
                row.append(0)
        row.reverse()
        
        for x in range(4):
            grid[y][x] = row[x]            