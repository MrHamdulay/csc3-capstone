"""Shriya Roy
1 May 2014
program to game"""
def push_up (grid):
    """merge grid values upwards"""
    
    
    for col in range(4):#moving up so column first
        for row in range(4):
            if row==3:
                continue # if true continue function
            if grid[row][col]==0:
                grid[row][col]=grid[row+1][col]
                grid[row+1][col]=0
        #moving down 3 times        
        for k in range(3,-1,-1):
            if grid[k][col]==grid[k-1][col]:# checking to see if numbers are equal
                grid[k-1][col]=grid[k-1][col]*2
                grid[k][col]=0
        for row in range(4):
            if row==3:
                continue           
            if grid[row][col]==0:
                grid[row][col]=grid[row+1][col]
                grid[row+1][col]=0  
        for row in range(4):
            if row==3:
                continue           
            if grid[row][col]==0:
                grid[row][col]=grid[row+1][col]
                grid[row+1][col]=0
        for row in range(4):
            if row==3:
                continue
            if grid[row][col]==0:
                grid[row][col]=grid[row+1][col]
                grid[row+1][col]=0


                
     

def push_down(grid):
    """merge grid values downwards"""
         
    for col in range(4):#moving down so start with column
        for row in range(3,-1,-1):
            if row==0:
                continue
            if grid[row][col]==0:
                grid[row][col]=grid[row-1][col]
                grid[row-1][col]=0
         #checking to see if numbers are equal           
        for k in range(4):
            if grid[k][col]==grid[k-1][col]:
                grid[k-1][col]=grid[k-1][col]*2#if numbers are equal< add together
                grid[k][col]=0
        for row in range(3,-1,-1):
            if row==0:
                continue           
            if grid[row][col]==0:
                grid[row][col]=grid[row-1][col]
                grid[row-1][col]=0  
        for row in range(3,-1,-1):
            if row==0:
                continue           
            if grid[row][col]==0:
                grid[row][col]=grid[row-1][col]
                grid[row-1][col]=0
        for row in range(3,-1,-1):
            if row==0:
                continue
            if grid[row][col]==0:
                grid[row][col]=grid[row-1][col]
                grid[row-1][col]=0
       


def push_left(grid):
    """merge grid values left"""
      
    

    
    for row in range(4):# start with row because moving left
        for col in range(4):
            if col==3:
                continue
            if grid[row][col]==0:#checking to see if numbers are equal
                grid[row][col]=grid[row][col+1]
                grid[row][col+1]=0
                
        for k in range(3,-1,-1):
            if grid[row][k]==grid[row][k-1]:
                grid[row][k-1]=grid[row][k-1]*2#if numbers are equal add them
                grid[row][k]=0
        for col in range(4):
            if col==3:
                continue           
            if grid[row][col]==0:
                grid[row][col]=grid[row][col+1]
                grid[row][col+1]=0  
        for col in range(4):
            if col==3:
                continue           
            if grid[row][col]==0:
                grid[row][col]=grid[row][col+1]
                grid[row][col+1]=0
        for col in range(4):
            if col==3:
                continue
            if grid[row][col]==0:
                grid[row][col]=grid[row][col+1]
                grid[row][col+1]=0
    
def push_right(grid):
    """merge grid values right"""
  
             
    for row in range(4):# start with row because moving right
        for col in range(3,-1,-1):
            if col==0:
                continue
            if grid[row][col]==0:#checking if position is zero
                grid[row][col]=grid[row][col-1]
                grid[row][col-1]=0
                    
        for k in range(4):
            if grid[row][k]==grid[row][k-1]:#checking if numbers are equal
                grid[row][k-1]=grid[row][k-1]*2#add numbers
                grid[row][k]=0
        for col in range(3,-1,-1):
            if col==0:
                continue           
            if grid[row][col]==0:
                grid[row][col]=grid[row][col-1]
                grid[row][col-1]=0  
        for col in range(3,-1,-1):
            if col==0:
                continue           
            if grid[row][col]==0:
                grid[row][col]=grid[row][col-1]
                grid[row][col-1]=0
        for col in range(3,-1,-1):
            if col==0:
                continue
            if grid[row][col]==0:
                grid[row][col]=grid[row][col-1]
                grid[row][col-1]=0
































