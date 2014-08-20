"""Assignment 7 question 3
Ross van der Heyde VHYROS001
30 April 2014"""

#def print_grid (grid): #works
    #"""print out a 4x4 grid in 5-width columns within a box"""
    #output = "{:<5}"
    #print("+--------------------+")
    #for i in range (4):#rows
        #print("|",end = "")
        #for j in range(4):#columns
            #if grid[i][j]!= 0:
                #print(output.format(grid[i][j]),end="")
            #else:
                #print(output.format(""),end="")
        #print("|")        
    #print("+--------------------+")

def push_up (grid):
    """merge grid values upwards"""
    
    #first move everything up
    moveUp(grid)
                
    #now merge values, replace spaces with 0
    for col in range (4):#cols
        for row in range (3): #rows     
            if grid [row][col]== grid[row+1][col]:
                grid [row][col]*=2
                grid [row+1][col] = 0 
                    
    #move up again
    moveUp(grid)
    
def push_down (grid):
    """merge grid values downwards"""
    #move everything down
    moveDown(grid)

    # merge
    for col in range (4):#cols
        for row in range (3,0,-1): #rows     
            if grid [row][col]== grid[row-1][col]:
                grid [row][col]*=2
                grid [row-1][col] = 0     
                        
    moveDown(grid)

def push_left (grid):
    """merge grid values left"""
    moveLeft(grid)
    
    #merge
    for row in range (4):#cols
        for col in range (3): #rows     
            if grid [row][col]== grid[row][col+1]:
                grid [row][col]*=2
                grid [row][col+1] = 0      
 
    moveLeft(grid)

def push_right (grid):
    """merge grid values right"""  
    moveRight(grid)
    
    #merge
    for row in range (4):#cols
        for col in range (3,0,-1): #rows     
            if grid [row][col]== grid[row][col-1]:
                grid [row][col]*=2
                grid [row][col-1] = 0     
    
    moveRight(grid)

def moveRight(grid):
    for i in range (4):
        for row in range (4):#cols
            for col in range (3,0,-1): #rows  
                    
                if grid [row][col] ==0 :# start at row 0, check if == 0
                    grid [row][col] = grid [row][col-1]
                    grid [row][col-1] = 0         

def moveLeft(grid):#DOES NOT WORK
    """Moves all values all the way left in row"""
    for i in range (4):
        for row in range (4):#cols
            for col in range (3): #rows  
                    
                if grid [row][col] ==0 :# start at row 0, check if == 0
                    grid [row][col] = grid [row][col+1]
                    grid [row][col+1] = 0     

def moveUp(grid):
    """Moves all values all the way up in column"""
    for i in range (4):
        for col in range (4):#cols
            for row in range (3): #rows  
                    
                if grid [row][col] ==0 :# start at row 0, check if == 0
                    grid [row][col] = grid [row+1][col]
                    grid [row+1][col] = 0 

def moveDown(grid):
    """Moves all values all the down up in column"""
    for i in range (4):
        for col in range (4):#cols
            for row in range (3,0,-1): #rows  
                    
                if grid [row][col] ==0 :
                    grid [row][col] = grid [row-1][col]
                    grid [row-1][col] = 0    
 
                        
#grid = [[2,2,2,2], #row 0
        #[512,0,512,0], #row 1
        #[8,0,2,0], #row 2
        #[0,16,0,16]] #row 3
#print_grid(grid)
#push_right(grid)
#print_grid(grid)