def push_up (grid):
    """merge grid values upwards"""
    for x in range(4):
        vert=[]       
        for y in range(4):
            vert.append(grid[y][x])
        vert=pushgrid(vert)            
        for y in range(4):
            grid[y][x]=vert[y]

def push_down (grid):
    """merge grid values downwards"""
    for x in range(4):
        vert=[]    
        for y in range(4):
            vert.append(grid[y][x])      
        vert.reverse()
        vert=pushgrid(vert)
        vert.reverse()    
        for y in range(4):
            grid[y][x]=vert[y]

def push_left (grid):
    """merge grid values left"""
    for y in range(4):
        row=[]    
        for x in range(4):
            row.append(grid[y][x])
        row=pushgrid(row)        
        for x in range(4):
            grid[y][x]=row[x]

def push_right (grid):
    """merge grid values right"""
    for y in range(4):
        row=[]
        for x in range(4):
            row.append(grid[y][x])      
        row.reverse()
        row=pushgrid(row)
        row.reverse()       
        for x in range(4):
            grid[y][x]=row[x]
    
def pushgrid(grid_0):
    """function used by other push functions to reduce redundancy of code"""
    grid=grid_0
    zeroes=0   
    for i in range(3):        
        if grid[i-zeroes]==0:
            del grid[i-zeroes]
            grid.append(0)
            zeroes+=1    
    for n in range(3):
        if grid[n]==grid[n+1]:
            grid[n]+=grid[n+1]
            del grid[n+1]
            grid.append(0)            
    return grid
            