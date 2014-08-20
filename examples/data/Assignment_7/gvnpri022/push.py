"""question 3-assignment 7- merging functions
GVNPRI022
02 May 2014"""
import util
def push_up(grid):
    #grid=[[2,0,2,0],[0,4,0,8],[2,16,0,128],[2,2,2,2]]
    #grid=[[2, 0, 2, 0], [2, 0, 2, 0], [2, 0, 2, 0], [2, 0, 2, 0]]
    #print(grid)
    for row in range(3,-1,-1): #starting from down and pushing up
        for col in range(4): 
            if row==0:
                if(grid[0][col]==0): #checking  case to know how many units to push up
                    
                    grid[0][col]=grid[1][col]
                    grid[1][col]=grid[2][col]
                    grid[2][col]=grid[3][col]
                    grid[3][col]=0
               
            if row==1:
                if(grid[1][col]==0):
                                        
                    
                    grid[1][col]=grid[2][col]
                    grid[2][col]=grid[3][col]
                    grid[3][col]=0                 
                 
            if row==2:
                if(grid[2][col]==0):
                                        
                    
                    grid[2][col]=grid[3][col]
                    grid[3][col]=0    
    #util.print_grid(grid) 
    
    for col in range(4): #going through columns to check if adjacent values are equal
    
                 
                   
            
        
       
            
            
        if(grid[0][col]==grid[1][col]):
                    
            grid[0][col]= 2*grid[0][col] #multiplying by 2
            grid[1][col]=grid[2][col]
            grid[2][col]=grid[3][col]
            grid[3][col]=0 
        
        if(grid[1][col]==grid[2][col]):
                           
            grid[1][col]= 2*grid[1][col]
            grid[2][col]=grid[3][col]
            grid[3][col]=0   
        
        if(grid[2][col]==grid[3][col]):
            grid[2][col]=2*(grid[2][col])
            grid[3][col]=0        
      
    
def push_down(grid): #starting from the top and pushing down
    for row in range(0,4):
        for col in range(4): 
            if row==3:
                if(grid[3][col]==0):
                    
                    grid[3][col]=grid[2][col]
                    grid[2][col]=grid[1][col]
                    grid[1][col]=grid[0][col]
                    grid[0][col]=0
                   
            if row==2:
                if(grid[2][col]==0):
                                            
                        
                    grid[2][col]=grid[1][col]
                    grid[1][col]=grid[0][col]
                    grid[0][col]=0                 
                     
            if row==1:
                if(grid[1][col]==0):
                                            
                        
                    grid[1][col]=grid[0][col]
                    grid[0][col]=0      
    
            

    for col in range(4):                       
                                     
                                       
                                
                            
                           
                                
                                
        if(grid[3][col]==grid[2][col]):
                                        
            grid[3][col]= 2*grid[3][col]
            grid[2][col]=grid[1][col]
            grid[1][col]=grid[0][col]
            grid[0][col]=0 
                            
        if(grid[2][col]==grid[1][col]):
                                               
            grid[2][col]= 2*grid[2][col]
            grid[1][col]=grid[0][col]
            grid[0][col]=0   
            
        if(grid[1][col]==grid[0][col]):
            grid[1][col]=2*(grid[1][col])
            grid[0][col]=0    




def push_right(grid): #starting from left and pushing right
    
    for col in range(4):
        for row in range(4):
            if col==1:
                if(grid[row][1]==0):
                                
                    grid[row][1]=grid[row][0]
                    grid[row][0]=0  
            
            
            if col==2:
                if(grid[row][2]==0):
                    grid[row][2]=grid[row][1]
                    grid[row][1]=grid[row][0]
                    grid[row][0]=0            
            
            if col==3:
                if(grid[row][3]==0):
                    grid[row][3]=grid[row][2]
                    grid[row][2]=grid[row][1]
                    grid[row][1]=grid[row][0]
                    grid[row][0]=0
            
            
            
                              
                    
    
    for row in range(4):
        if(grid[row][3]==grid[row][2]):
            grid[row][3]= 2*grid[row][3]
            grid[row][2]=grid[row][1]
            grid[row][1]=grid[row][0]
            grid[row][0]=0
        
        if(grid[row][2]==grid[row][1]):
            grid[row][2]= 2*grid[row][2]
            grid[row][1]=grid[row][0]
            grid[row][0]=0            
    
        
        if (grid[row][1]==grid[row][0]):
            grid[row][1]=grid[row][1]*2
            grid[row][0]=0


def push_left(grid): #starting from right and pushing left
    
    for col in range(3,-1,-1):
            for row in range(4):
                if col==0:
                    if(grid[row][0]==0):
                                    
                        grid[row][0]=grid[row][1]
                        grid[row][1]=grid[row][2]
                        grid[row][2]=grid[row][3]
                        grid[row][3]=0
                
                
                if col==1:
                    if(grid[row][1]==0):
                        grid[row][1]=grid[row][2]
                        grid[row][2]=grid[row][3]
                        grid[row][3]=0           
                
                if col==2:
                    if(grid[row][2]==0):
                        grid[row][2]=grid[row][3]
                        grid[row][3]=0    
    
    for row in range(4):
        if(grid[row][0]==grid[row][1]):
            grid[row][0]= 2*grid[row][1]
            grid[row][1]=grid[row][2]
            grid[row][2]=grid[row][3]
            grid[row][3]=0
                
        if(grid[row][1]==grid[row][2]):
            grid[row][1]= 2*grid[row][1]
            grid[row][2]=grid[row][3]
            grid[row][3]=0            
            
                
        if (grid[row][2]==grid[row][3]):
            grid[row][2]=grid[row][2]*2
            grid[row][3]=0        