#Module containing merging fuctions for the 2048 game
#Nevarr Pillay - PLLNEV006
#1 May 2014

def move(grid,i,start,end,jump,direction):
    """If a zero is found in the direction of movement, the numbers are moved that way to fill up the gap"""
    #If the direction is up or down
    if direction == "u" or direction == "d":
        for times in range(numofnums(grid,i,len(grid[i]),"ud")):
            for k in range(start,end,jump):
                #Checks in direction of jump (+ or -)
                if grid[k+jump][i] == 0:
                    grid[k+jump][i],grid[k][i] = grid[k][i],0    
    #If the direction is left or right            
    elif direction == "l" or direction == "r":
        for times in range(numofnums(grid,i,len(grid[i]),"ud")):
            for k in range(start,end,jump):   
                if grid[i][k+jump] == 0:
                    grid[i][k+jump],grid[i][k] = grid[i][k],0         
                
def merge(grid,i,start,end,jump,direction): 
    """If the number adjacent to the current is equal, they are added together and the block below is set to 0"""
    if direction == "u" or direction == "d":        
        for j in range(start,end,jump):
            if grid[j][i] == grid[j+jump][i] and grid[j][i] != 0:
                grid[j][i], grid[j+jump][i] = grid[j][i]+grid[j+jump][i],0    
    elif direction == "l" or direction == "r":
        for j in range(start,end,jump):
            if grid[i][j] == grid[i][j+jump] and grid[i][j] != 0:
                grid[i][j], grid[i][j+jump] = grid[i][j]+grid[i][j+jump],0       
                
def numofnums(grid,i,stop,direction):
    count = 1
    if direction == "ud":
        for j in range(stop):
            if grid[j][i] != 0:
                count += count
    if direction == "lr":
        for j in range(stop):
            if grid[i][j] != 0:
                count += count       
    return count            

def push_up(grid):
    """Pushes all values upwards, merging adjacent values that are equal"""
    for i in range(len(grid)):  
        #Goes through each column in the grid or row
        move(grid,i,len(grid[i])-1,0,-1,"u") 
        merge(grid,i,0,len(grid[i])-1,1,"u")
        move(grid,i,len(grid[i])-1,0,-1,"u")        
              
                    
def push_down(grid):
    """Pushes all values downwards, merging adjacent values that are equal"""
    for i in range(len(grid)):
        #Goes through each column in the grid or row
        move(grid,i,0,len(grid[i])-1,1,"d") 
        merge(grid,i,len(grid[i])-1,0,-1,"d")
        move(grid,i,0,len(grid[i])-1,1,"d")               

def push_left(grid):
    """Pushes all values to the left, merging adjacent values that are equal"""
    for i in range(len(grid)):
        #Goes through each column in the grid or row
        move(grid,i,len(grid[i])-1,0,-1,"l") 
        merge(grid,i,0,len(grid[i])-1,1,"l")
        move(grid,i,len(grid[i])-1,0,-1,"l")  
                
def push_right(grid):
    """Pushes all values to the right, merging adjacent values that are equal"""
    for i in range(len(grid)):
        #Goes through each column in the grid or row
        move(grid,i,0,len(grid[i])-1,1,"r") 
        merge(grid,i,len(grid[i])-1,0,-1,"r")
        move(grid,i,0,len(grid[i])-1,1,"r")           
            