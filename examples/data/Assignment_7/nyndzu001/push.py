"""Dzunisani Nyoni
30 April 2014
A program to make the game 2048"""

height=4

def push(var):
    """A fuction to push the numbers"""
    for row in range(var.count(0)):
        col=0
        while col<3:
            if var[col]==0:
                var[col]=var[col+1]
                var[col+1]-=var[col+1]
            col+=1
    return var
def add(var):
    """Adds nummbers when they are equal"""
    count = 0
    while count < 3:
        if var[count] == var[count+1]:
            var[count] *= 2
            var[count+1] *= 0
        count += 1
    return var
    
def push_up (grid):
    """Pushes the numbers up and merges them"""
    for row in range(height):
        column=[]
        for col in range(height):
            column.append(grid[col][row])      
        push(column)
        add(column)
        push(column)

        for j in range(height):
            grid[j][row] = column[j]
          
            
def push_down (grid):
    """Pushes the numbers up and merges the numbers"""    
    for row in range(height):
        column = []
        for col in range(3,-1,-1):
            column.append(grid[col][row])
        push(column)
        add(column)
        push(column)
        counter=0
        for i in range(3,-1,-1):
            grid[i][row] = column[counter]
            counter+=1
    
    
    
def push_left (grid):
    """Pushes the numbers to the left and merges them"""
    for row in range(height):
        grids = []
        for col in range(height):
            grids.append(grid[row][col])
        push(grids)
        add(grids)
        push(grids)        
        
        for i in range(height):
            grid[row][i] = grids[i]

def push_right (grid):
    #merge grid values right 
    for row in range(height):
        count=0
        grids = []
        for col in range(3,-1,-1):
            grids.append(grid[row][col])
        push(grids)
        add(grids)
        push(grids)
        
        for col in range(3,-1,-1):
            grid[row][col] = grids[count]
            count+=1
                    
    
    