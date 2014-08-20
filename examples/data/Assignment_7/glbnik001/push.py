# Notes on writing these functons:
#follow three step process each time
#remove 0's, combine values, remove zeros again (not sure why run into problems when i dont)

def push_up(grid):
    # Top values must stay the same so iterate for all values below the first horizontal line
    for horz in range (1,4):
        for vert in range (4):
            if grid [horz-1][vert]==" " or grid[horz-1][vert]==0:
                grid [horz-1][vert] = grid[horz][vert]
                grid [horz][vert] = 0 #deletes the bottom row because it merged with the top 
                
    #This paragraph merges the lines when the numbers above are the same
    for horz in range (1,4):
        for vert in range (4):
            if grid [horz-1][vert] == grid[horz][vert]:
                grid[horz-1][vert] = grid[horz-1][vert] * 2 #adds the lines together, can use the same reference point because the numbers are identical
                grid[horz][vert] = 0
    
    for horz in range (1,4):
        for vert in range (4):
            if grid [horz-1][vert] == " " or grid[horz-1][vert]==0:
                grid[horz-1][vert] = grid[horz][vert]
                grid[horz][vert] = 0    


def push_down(grid):
    #has to iterate backwards this time
    #start from third horizontal line
    #use + this time because its the one above
    for horz in range (2,-1,-1):
        for vert in range(4):
            if grid[horz+1][vert] == " " or grid[horz+1][vert]==0:
                grid[horz+1][vert] = grid[horz][vert]
                grid[horz+1][vert] = 0 #deletes all items that have been removed 
    
    for horz in range (2,-1,-1):
        for vert in range (4):
            if grid[horz+1][vert]==grid[horz][vert]:
                grid[horz+1][vert]= grid[horz+1][vert] * 2
                grid[horz][vert]=0
    
    for horz in range (2,-1,-1):
        for vert in range (4):
            if grid[horz+1][vert]== " " or grid[horz+1][vert]==0:
                grid[horz+1][vert] = grid[horz][vert]
                grid[horz][vert]=0    

def push_right(grid):
    # this time we move to the right
    #has to iterate in the opposite diretion to accomodate, starts from the end
    for vert in range(2,-1,-1):
        for horz in range(4):
            if grid[horz][vert+1]==" " or grid[horz][vert+1]==0:
                grid[horz][vert+1]=grid[horz][vert+1]
                grid[horz][vert]=0
    
    for vert in range(2,-1,-1):
        for horz in range(4):
            if grid[horz][vert+1]==grid[horz][vert+1]:
                grid[horz][vert+1]=grid[horz][vert+1]*2
                grid[horz][vert]=0
    
    for vert in range(2,-1,-1):
        for horz in range(4):
            if grid[horz][vert+1]==" " or grid[horz][vert+1]==0:
                grid[horz][vert+1]=grid[horz][vert]
                grid[horz][vert]=0


def push_left(grid):
    #iterate forward 
    #doesnt manipulate the leftmost line going down
    for vert in range(1,4):
        for horz in range(4):
            if grid[horz][vert-1]==" " or grid[horz][vert-1]==0:
                grid[horz][vert-1] = grid[horz][vert]
                grid[horz][vert]=0
    
    for vert in range(1,4):
        for horz in range(4):
            if grid[horz][vert-1]==grid[horz][vert]:
                grid[horz][vert-1]=grid[horz][vert-1]*2
                grid[horz][vert]=0
    
    for vert in range(1,4):
        for horz in range(4):
            if grid[horz][vert-1]==" " or grid[horz][vert-1]==0:
                grid[horz][vert-1]=grid[horz][vert]
                grid[horz][vert]=0
    

    
    
                
