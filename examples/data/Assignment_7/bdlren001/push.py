
# To create a code for the 2048 game
# Budeli Rendani
# BDLREN001
# 01/04/2014

# function needed for adding the values
def adding(x):
    y=0
    j = y
    while j < 3:
        if x[j] == x[j+1]:
            x[j] *= 2
            x[j+1] *= 0
        j=j+1
    return x

# Funtion needed for pushing the values
def pushing(x):
    for row in range(x.count(0)):
        y=0
        col=y
        while col<3:
            if x[col]==0:
                x[col]=x[col+1]
                x[col+1]-=x[col+1]
            col=col+1
    return x

# Merging and pushing values up
def push_up (grid):
    for row in range(4):
        column=[]
        for col in range(4):
            column.append(grid[col][row])      
        pushing(column)
        adding(column)
        pushing(column)

        for i in range(4):
            grid[i][row] = column[i]
          
# Merging and pushing values down
def push_down (grid):
    c=[]
    for row in range(4):
        for col in range(3,-1,-1):
            c.append(grid[col][row])
        pushing(c)
        adding(c)
        pushing(c)
        y=0
        x=y
        for i in range(3,-1,-1):
            grid[i][row] = c[x]
            x=x+1

# Merging and pushing values to the right
def push_right (grid):
    r=[] 
    for row in range(4):
        for col in range(3,-1,-1):
            r.append(grid[row][col])
        pushing(r)
        adding(r)
        pushing(r)
        y=0
        x=y
        for i in range(3,-1,-1):
            grid[row][i] = r[x]
            x=x+1
                    
# Merging and pushing values to the left
def push_left (grid):
    for row in range(4):
        rows = []
        for col in range(4):
            rows.append(grid[row][col])
        pushing(rows)
        adding(rows)
        pushing(rows)        
        
        for i in range(4):
            grid[row][i] = rows[i]    
    