"""mokoena mafologele
program to push numbers in 2048
02/05/2014
"""
import util
def push_up (grid):
    """push up and merge values upwards"""
    for col in range(4):
        #moves values upwards
        for row in range(3):
            c=row+1
            if grid[row][col]==0:
                while grid[row][col]==0 and c<4:
                    grid[row][col]=grid[c][col]
                    grid[c][col]=0
                    c+=1
        #add vertical numbers upwards        
        for i in range(0,3,1):
            if grid[i][col]==grid[i+1][col]:
                grid[i][col]=grid[i][col]*2
                grid[i+1][col]=0
        #merges numbers together again
        for row in range(3):
            c=row+1
            if grid[row][col]==0:
                while grid[row][col]==0 and c<4:
                    grid[row][col]=grid[c][col]
                    grid[c][col]=0
                    c+=1        
def push_down (grid):
    #merge downwards
    for col in range(4):
        #move grid values downwards
        for row in range(3,0,-1):
            c=row-1
            if grid[row][col]==0:
                while grid[row][col]==0 and c>=0:
                    grid[row][col]=grid[c][col]
                    grid[c][col]=0
                    c-=1
        #add vertical numbers downwards       
        for i in range(3,0,-1):
            if grid[i][col]==grid[i-1][col]:
                grid[i][col]=grid[i][col]*2
                grid[i-1][col]=0
                
        #merges numbers together again
        for row in range(3,0,-1):
            c=row-1
            if grid[row][col]==0:
                while grid[row][col]==0 and c>=0:
                    grid[row][col]=grid[c][col]
                    grid[c][col]=0
                    c-=1        
def push_right (grid):
    #merge to the right
    for row in range(4):
        #move grid values right
        for col in range(3,0,-1):
            c=col-1
            if grid[row][col]==0:
                while grid[row][col]==0 and c>=0:
                    grid[row][col]=grid[row][c]
                    grid[row][c]=0
                    c-=1
                    
        #add horizontal numbers to the right
        for i in range(3,0,-1):
            if grid[row][i]==grid[row][i-1]:
                grid[row][i]=grid[row][i]*2
                grid[row][i-1]=0
        
        #merge numbers back together again
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
    #merge left      
    for row in range(4):
        
        #move grid values left
        for col in range(3):
            c=col+1
            if grid[row][col]==0:
                while grid[row][col]==0 and c<4:
                    grid[row][col]=grid[row][c]
                    grid[row][c]=0
                    c+=1
        
        #add horizontal numbers        
        for i in range(0,3,1):
            if grid[row][i]==grid[row][i+1]:
                grid[row][i]=grid[row][i]*2
                grid[row][i+1]=0
        
        #merge together again
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
