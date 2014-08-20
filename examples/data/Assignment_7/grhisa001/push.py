""" Bella Gorham
2043 game
30/04/14"""


def move_upwards (grid):
    
    #move all items up
    for row in range(4):
        for col in range(4):
            # check if there is a value
            if grid[row][col] != False :
                for remrow in range(row):
                    #check to see of the rows above are empty
                    if grid[remrow][col]==0:
                       
                        #move up columns into empty space
                        grid[remrow][col]=grid[row][col]
                        #make empty space where coloum item was
                        grid[row][col]=0
                        
    
    return grid

def add_up(grid):
    for row in range(4):
        for col in range(4):
        
            if row != 3 and grid[row][col]==grid[row+1][col]:
                grid[row][col]+=grid[row+1][col]
                if row < 0:
                    grid[row+1][col]=grid[row+2][col]
                
                else:
                    grid[row+1][col]=0
               
    return grid


def move_downwards(grid):
    
    #move all items up
    for row in range(4):
        for col in range(4):
            # check if there is a value
            if grid[row][col] != False :
                for remrow in range(row,4):
                    #check to see of the rows above are empty
                    if grid[remrow][col]==0:
                           
                        #move up columns into empty space
                        grid[remrow][col]=grid[row][col]
                        #make empty space where coloum item was
                        grid[row][col]=0
    return grid

def add_down(grid):
   
    for row in range(4):
        for col in range(4):
        
            if row != 3 and grid[row][col]==grid[row+1][col]:
                grid[row][col]+=grid[row+1][col]
                if row < 0:
                    grid[row+1][col]=grid[row+2][col]
                
                else:
                    grid[row+1][col]=0
               
    return grid



def move_leftwards(grid):
    
    #move all items up
    for row in range(4):
        for col in range(4):
        # check if there is a value
            if grid[row][col] != False :
                for remcol in range(col):
                    #check to see of the col above are empty
                    if grid[row][remcol]==0:
                               
                        #move up columns into empty space
                        grid[row][remcol]=grid[row][col]
                        #make empty space where coloum item was
                        grid[row][col]=0    
    return grid
def add_left(grid):
    
    for row in range(4):
        for col in range(4):
            
            if col!=3  and grid[row][col]==grid[row][col+1]:
                grid[row][col]+=grid[row][col+1]
              
                
                if col < 0:
                    grid[row][col+1]=grid[row][col+2]
                    
                else:
                    grid[row][col+1]=0
                   
    return grid    

def move_rightwards(grid):
   
    #move all items up
    for row in range(4):
        for col in range(4):
        # check if there is a value
            if grid[row][col] != False :
                for remcol in range(col,4):
                    #check to see of the col above are empty
                    if grid[row][remcol]==0:
                               
                        #move up columns into empty space
                        grid[row][remcol]=grid[row][col]
                        #make empty space where coloum item was
                        grid[row][col]=0 
    return grid
                        
                        
def add_right(grid):
    
    for row in range(4):
        for col in range(4):
            
            if col!=3  and grid[row][col]==grid[row][col+1]:
                grid[row][col]+=grid[row][col+1]
              
                
                if col < 0:
                    grid[row][col+1]=grid[row][col+2]
                    
                else:
                    grid[row][col+1]=0
    return grid
                   
    
    
def push_down(grid):
    moved1=move_downwards(grid)
    added1=add_down(moved1)
    moved2=move_downwards(added1)
    return moved2   

def push_left(grid):
    moved1=move_leftwards(grid)
    added1=add_left(moved1)
    moved2=move_leftwards(added1)
    return moved2  

def push_right(grid):
    moved1=move_rightwards(grid)
    added1=add_right(moved1)
    moved2=move_rightwards(added1)
    return moved2 

def push_up (grid):
    moved1=move_upwards(grid)
    added1=add_up(moved1)
    moved2=move_upwards(added1)
    return moved2

    
    
    
    
if __name__=='__main__':

    testgrid=([[0,0,0,0],[0,0,0,0],[0,0,2,0],[2,0,0,0]])
    
    
    
    push_right(testgrid) 
    
    push_up (testgrid)
    
    push_down(testgrid)
    
    push_left(testgrid)