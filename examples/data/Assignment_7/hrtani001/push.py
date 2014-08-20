#Aniq Hartle
#02/05/2014
#functions for shifting tiles in  2048 game

#shift all tiles up
def push_up(grid):#shifts all tiles to max possible height
    for repeat in range(4):
        for row in range(3,0,-1):
            for col in range(0,4):
                if grid[row-1][col] == 0:
                    grid[row-1][col] = grid[row][col]
                    grid[row][col] = 0                     
    for row in range(0,3):#starting from the top, combines duplicate tiles(values)
        for col in range(0,4):
            if grid[row][col]==grid[row+1][col]:
                grid[row][col] = grid[row][col]*2
                grid[row+1][col]=0        
    for repeat in range(4):#again shifts all tiles up to maximun height
        for row in range(3,0,-1):
            for col in range(0,4):
                if grid[row-1][col] == 0:
                    grid[row-1][col] = grid[row][col]
                    grid[row][col]=0  
                    
'''for row in range(0,4):
        for col in range(0,3):    
            if grid[row][col] == 0:
                grid[row][col] = grid[row][col+1] 
                grid[row][col+1]=0    '''
    

def push_down(grid):#Shifts all tiles down using same basic concept as push_up
    for repeat in range(4):
        for row in range(2,-1,-1):
            for col in range(0,4):
                if grid[row+1][col] == 0:
                    grid[row+1][col] = grid[row][col]
                    grid[row][col] = 0 
    for row in range(2,-1,-1):
        for col in range(0,4):
            if grid[row][col]==grid[row+1][col]:
                grid[row+1][col] = grid[row+1][col]*2
                grid[row][col]=0                
    for repeat in range(4):
        for row in range(2,-1,-1):
            for col in range(0,4):
                if grid[row+1][col] == 0:
                    grid[row+1][col] = grid[row][col]
                    grid[row][col] = 0 
                    
'''for row in range(0,4):
        for col in range(0,3):    
            if grid[row][col] == 0:
                grid[row][col] = grid[row][col+1] 
                grid[row][col+1]=0    '''

def push_left(grid):#Shifts all tiles left using same basic concept as push_up
    for repeat in range(4):
        for row in range(0,4):
            for col in range(3,0,-1):
                if grid[row][col-1] == 0:
                    grid[row][col-1] = grid[row][col]
                    grid[row][col] = 0                     
    for row in range(0,4):
        for col in range(0,3):
            if grid[row][col]==grid[row][col+1]:
                grid[row][col] = grid[row][col]*2
                grid[row][col+1]=0        
    for repeat in range(4):
        for row in range(0,4):
            for col in range(3,0,-1):
                if grid[row][col-1] == 0:
                    grid[row][col-1] = grid[row][col]
                    grid[row][col]=0   
   
                    
'''for row in range(0,4):
        for col in range(0,3):    
            if grid[row][col] == 0:
                grid[row][col] = grid[row][col+1] 
                grid[row][col+1]=0    '''

def push_right(grid):#Shifts all tiles right using same basic concept as push_up
    for repeat in range(4):
        for row in range(0,4):
            for col in range(0,3):
                if grid[row][col+1] == 0:
                    grid[row][col+1] = grid[row][col]
                    grid[row][col] = 0                     
    for row in range(0,4):
        for col in range(3,0,-1):
            if grid[row][col]==grid[row][col-1]:
                grid[row][col] = grid[row][col]*2
                grid[row][col-1]=0        
    for repeat in range(4):
        for row in range(0,4):
            for col in range(0,3):
                if grid[row][col+1] == 0:
                    grid[row][col+1] = grid[row][col]
                    grid[row][col]=0   
   #return grid
    
'''for row in range(0,4):
        for col in range(0,3):    
            if grid[row][col] == 0:
                grid[row][col] = grid[row][col+1] 
                grid[row][col+1]=0    '''


                
'''def print_grid(grid):
    print("+--------------------+")
    for i in range(len(grid)):
        print("|",end="")
        for j in range(len(grid)):
            print(grid[i][j]," "*(4-len(str(grid[i][j]))), end="")
        print("|")
    print("+--------------------+")
            

grid = [[4,4,8,8],[2,8,4,2],[2,2,2,16],[16,2,2,4]]

print_grid(grid)
print_grid(push_right(grid))'''