#Amitha Doodnath
#DDNAMI001
#01/05/2014
#Programme of push functions for 2048.py
import util

def push_left(grid):
    
    for i in range (4):
        for j in range (4):
            #shifts grid left
            if int(grid[i][0]) ==0:
                del grid[i][0]
                grid[i].append(0)
                
            if int(grid[i][1]) ==0:
                del grid[i][1]
                grid[i].append(0)
                
            if int(grid[i][2]) ==0:
                del grid[i][2]
                grid[i].append(0)
            
            if int(grid[i][3]) ==0:
                del grid[i][3]
                grid[i].append(0) 
                
    #adds if adjacent values equal            
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] += grid[i][j+1]
                del grid[i][j+1]
                grid[i].append(0)


def push_right(grid):
    
    for i in range (4):
        for j in range (4):
            #shifts grid right
            if int(grid[i][0]) ==0:
                del grid[i][0]
                grid[i].insert(0,0)
                
            if int(grid[i][1]) ==0:
                del grid[i][1]
                grid[i].insert(0,0)
                
            if int(grid[i][2]) ==0:
                del grid[i][2]
                grid[i].insert(0,0)
            
            if int(grid[i][3]) ==0:
                del grid[i][3]
                grid[i].insert(0,0) 
                
    #adds if adjacent values equal            
    for i in range(4):
        for j in range(1,4):
            if grid[i][j] == grid[i][j-1]:
                grid[i][j] += grid[i][j-1]
                del grid[i][j-1]
                grid[i].insert(0,0)


def push_up(grid):
    #shifts grid up
    for j in range(4):
        for i in range(4):
            if grid[0][j]==0:
                grid[0][j],grid[1][j],grid[2][j],grid[3][j] = grid[1][j],grid[2][j],grid[3][j],grid[0][j]
                
        
            if grid[1][j]==0:
                grid[1][j],grid[2][j],grid[3][j]=grid[2][j],grid[3][j],grid[1][j]
                        
            
            if grid[2][j]==0:
                grid[2][j],grid[3][j]=grid[3][j],grid[2][j]
    
    #adds adjacent values and shifts grid up            
    for i in range(4):
        for j in range(4):
            if grid[0][j]== grid[1][j]:
                grid[0][j],grid[1][j],grid[2][j],grid[3][j] = (grid[0][j]+grid[1][j]),grid[2][j],grid[3][j],0
                
                
                
        
            if grid[1][j]==grid[2][j]:
                grid[1][j],grid[2][j],grid[3][j]=(grid[1][j]+grid[2][j]),grid[3][j],0
                
                        
            
            if grid[2][j]==grid[3][j]:
                grid[2][j],grid[3][j]=(grid[2][j]+grid[3][j]),0
                
        break
                
                


def push_down(grid):
    #shifts grid down
    for j in range(4):
        for i in range(4):
            if grid[3][j]==0:
                grid[3][j],grid[2][j],grid[1][j],grid[0][j] = grid[2][j],grid[1][j],grid[0][j],grid[3][j]
                
        
            if grid[2][j]==0:
                grid[2][j],grid[1][j],grid[0][j]=grid[1][j],grid[0][j],grid[2][j]
                        
            
            if grid[1][j]==0:
                grid[1][j],grid[0][j]=grid[0][j],grid[1][j]
    
    #adds adjacent values and shifts grid down            
    for i in range(3):
        for j in range(4):
            if grid[3][j]== grid[2][j]:
                grid[3][j],grid[2][j],grid[1][j],grid[0][j] = (grid[3][j]+grid[2][j]),grid[1][j],grid[0][j],0
                
        
            if grid[2][j]==grid[1][j]:
                grid[2][j],grid[1][j],grid[0][j]=(grid[2][j]+grid[1][j]),grid[0][j],0
                
                        
            
            if grid[1][j]==grid[0][j]:
                grid[1][j],grid[0][j]=(grid[1][j]+grid[0][j]),0
                
        break
                           

                            
            
         