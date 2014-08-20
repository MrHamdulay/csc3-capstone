#MIla Tshaka
#2nd May 2014
import util
def push_up (grid):
    #merges the grid values upwards
    for col in range(4):
        #moves all grid values upwards
        for row in range(3):
            c=row+1
            if grid[row][col]==0:
                while grid[row][col]==0 and c<4:
                    grid[row][col]=grid[c][col]
                    grid[c][col]=0
                    c+=1
        #adds all numbers that are vertically adjacent to one another in an upward direction        
        for i in range(0,3,1):
            if grid[i][col]==grid[i+1][col]:
                grid[i][col]=grid[i][col]*2
                grid[i+1][col]=0
        #merges the numbers back together
        for row in range(3):
            c=row+1
            if grid[row][col]==0:
                while grid[row][col]==0 and c<4:
                    grid[row][col]=grid[c][col]
                    grid[c][col]=0
                    c+=1        
def push_down (grid):
    #merges grid values downwards
    for col in range(4):
        #moves all grid values downwards
        for row in range(3,0,-1):
            c=row-1
            if grid[row][col]==0:
                while grid[row][col]==0 and c>=0:
                    grid[row][col]=grid[c][col]
                    grid[c][col]=0
                    c-=1
        #adds all numbers that are vertically adjacent to one another in a downward direction        
        for i in range(3,0,-1):
            if grid[i][col]==grid[i-1][col]:
                grid[i][col]=grid[i][col]*2
                grid[i-1][col]=0
                
        #merges the numbers back together
        for row in range(3,0,-1):
            c=row-1
            if grid[row][col]==0:
                while grid[row][col]==0 and c>=0:
                    grid[row][col]=grid[c][col]
                    grid[c][col]=0
                    c-=1        
def push_right (grid):
    #merge grid values right
    for row in range(4):
        #moves all grid values to the right
        for col in range(3,0,-1):
            c=col-1
            if grid[row][col]==0:
                while grid[row][col]==0 and c>=0:
                    grid[row][col]=grid[row][c]
                    grid[row][c]=0
                    c-=1
                    
        #adds all numbers that are horizontally adjacent to one another to the right
        for i in range(3,0,-1):
            if grid[row][i]==grid[row][i-1]:
                grid[row][i]=grid[row][i]*2
                grid[row][i-1]=0
        
        #merges the numbers back together
        for row in range(3,0,-1):
            c=col-1
            if grid[row][col]==0:
                while grid[row][col]==0 and c>=0:
                    grid[row][col]=grid[row][c]
                    grid[row][c]=0
                    c-=1
        for j in range(1,3,1):
            if grid[row][j]==0:
                if grid[row][j-1]!=0:
                    grid[row][j]=grid[row][j-1]
                    grid[row][j-1]=0
def push_left (grid):
    #merges grid values left      
    for row in range(4):
        
        #moves all grid values to the left
        for col in range(3):
            c=col+1
            if grid[row][col]==0:
                while grid[row][col]==0 and c<4:
                    grid[row][col]=grid[row][c]
                    grid[row][c]=0
                    c+=1
        
        #adds all numbers that are horizontally adjacent to one another to the left        
        for i in range(0,3,1):
            if grid[row][i]==grid[row][i+1]:
                grid[row][i]=grid[row][i]*2
                grid[row][i+1]=0
        
        #merges the numbers back together
        for col in range(3):
            c=col+1
            if grid[row][col]==0:
                while grid[row][col]==0 and c<4:
                    grid[row][col]=grid[row][c]
                    grid[row][c]=0
                    c+=1  
                    
        for j in range(0,3,1):
            if grid[row][j]==0:
                if grid[row][j+1]!=0:
                    grid[row][j]=grid[row][j+1]
                    grid[row][j+1]=0        