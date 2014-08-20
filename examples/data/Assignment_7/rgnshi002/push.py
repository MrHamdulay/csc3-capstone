#Shivam Ragoonaden
#rgnshi002
#29 April 2014
#2048 left, up, down, right functions


def push_up (grid):
    """merge grid values upwards"""
    for i in range (3):   #Repeat 3 times 
        for row in range(1,4):  #Starts from 1 since we don't need top row as the item wouldn't need to move
            for col in range(4): #Check all columns
                if grid[row-1][col] == grid[row-1][col] ==0:  
                    grid[row-1][col] = grid[row][col]  #Make the item in the row below equal to the current item
                    grid[row][col] = 0  #And make the original item 0
                   
    for row in range(1,4):
        for col in range(4):
            if grid[row-1][col] == grid[row][col]:   #Check if they are the same
                grid[row][col] = 0  #Make original item 0                
                grid[row-1][col] = grid[row-1][col] *2  #"Merge" by multiplying item by 2
                
    for row in range(1,4):  #Last repetition of the i loop after merging
        for col in range(4):
            if grid[row-1][col] == grid[row-1][col] == 0:
                grid[row-1][col] = grid[row][col]
                grid[row][col] = 0

def push_down (grid):
    """merge grid values downwards"""
    for i in range (3):  #Repeat 3 times
        for row in range (2,-1,-1):  #Range goes backwards (pushing down), starts from 2 since we don't need the bottom row for similar reasons as above
            for col in range (3,-1,-1):  #Check all columns backwards
                if grid[row+1][col] == grid[row+1][col] ==0:  
                    grid[row+1][col] = grid[row][col]  #Make the item in the row above equal to the current item
                    grid[row][col] = 0  #And make the original item 0
                      
    for row in range(2,-1,-1):
        for col in range(3,-1,-1):
            if grid[row+1][col] == grid[row][col]: #Check if they are the same
                grid[row][col] = 0 #Make original item 0                
                grid[row+1][col] = grid[row+1][col] *2 #"Merge"
                   
    for row in range(2,-1,-1):  #Last repetition of the i loop after merging
        for col in range(3,-1,-1):
            if grid[row+1][col] == grid[row+1][col] == 0:
                grid[row+1][col] = grid[row][col]
                grid[row][col]=0 

def push_left (grid):
    """merge grid values left"""
    for i in range (3):   #Repeat 3 times
        for row in range(4):  #Check all rows
            for col in range(1,4): #Starts from 1 since we don't need first column as the item wouldn't need to move
                if grid[row][col-1] == grid[row][col-1] ==0:
                    grid[row][col-1] = grid[row][col]  #Make the item in the column leftwards of current item equal to current item
                    grid[row][col] = 0  #Make current item 0
                      
    for row in range(4):
        for col in range(1,4):  #Rest of left and right functions follow same principles as up and down functions, but for columns instead of rows
            if grid[row][col-1] == grid[row][col]:
                grid[row][col-1] = grid[row][col] *2
                grid[row][col] =0
                   
    for row in range(4):
        for col in range(1,4):
            if grid[row][col-1] == grid[row][col-1] == 0:
                grid[row][col-1] = grid[row][col]
                grid[row][col]=0    

def push_right (grid):
    """merge grid values right""" 
    for i in range (3):
        for row in range(3,-1,-1):
            for col in range(2,-1,-1):
                if grid[row][col+1] == grid[row][col+1] ==0:
                    grid[row][col+1] = grid[row][col]
                    grid[row][col] = 0
                      
    for row in range(3,-1,-1):
        for col in range(2,-1,-1):
            if grid[row][col+1] == grid[row][col]:
                grid[row][col] = 0                
                grid[row][col+1] = grid[row][col+1] *2
                   
    for row in range(3,-1,-1):
        for col in range(2,-1,-1):
            if grid[row][col+1] == grid[row][col+1] == 0:
                grid[row][col+1] = grid[row][col]
                grid[row][col]=0   