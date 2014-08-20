#2048 merging values
#Devaksha Pillay
#1 May 2014

         
           
def push_up(grid):
    #merge values upwards
    for columns in range(4):
        for rows in range(3):
            l = columns - 1
            r = columns + 1
            t = rows - 1
            b = rows + 1            
            value = grid[rows][columns]
            if value == grid[b][columns]:
                value = grid[b][columns]*2
                grid[b][columns] = 0
            
def push_down(grid):
    #merge values downwards
    for columns in range(4):
        for rows in range(3):
            l = columns - 1
            r = columns + 1
            t = rows - 1
            b = rows + 1            
            value = grid[rows][columns]
            if value == grid[t][columns]:
                value = grid[t][columns]*2
                grid[t][columns] = 0

def push_left(grid):
    #merge values left
    for rows in range(4):
        for columns in range(3):
            l = columns - 1
            r = columns + 1
            t = rows - 1
            b = rows + 1            
            value = grid[rows][columns]
            if value == grid[rows][r]:
                value = grid[rows][r]*2
                grid[rows][r] = 0
                
def push_right(grid):
    #merge values right
    for rows in range(4):
        for columns in range(3):
            l = columns - 1
            r = columns + 1
            t = rows - 1
            b = rows + 1            
            value = grid[rows][columns]
            if value == grid[rows][l]:
                value = grid[rows][l]*2
                grid[rows][l] = 0