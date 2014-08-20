# to complete the code for a 2048 program
# mashau zwivhuya
# 1 may 2014
def push_up (grid):
        #0  [0,0,0,0],
        #1  [0,0,0,0],
        #2  [0,0,0,0],
        #3  [0,0,0,0]
        
        
                                                 
        #move values 3 times
  
        for x in range(3):
                for y in range(4):
                        if grid[x][y] == 0:
                                grid[x][y] = grid[x+1][y]        
                                grid[x+1][y] = 0    

                                
        for x in range(3):
                for y in range(4):
                        if grid[x][y] == 0:
                                grid[x][y] = grid[x+1][y]        
                                grid[x+1][y] = 0                            
                                                        
        for x in range(3):
                for y in range(4):
                       if grid[x][y] == 0:
                               grid[x][y] = grid[x+1][y]        
                               grid[x+1][y] = 0 
                               

        #adds same numbers
        for x in range(3):
                for y in range(4):
                        if grid[x+1][y] == grid[x][y]:
                                        grid[x][y] = grid[x+1][y] + grid[x][y]        
                                        grid[x+1][y] = 0 
                                        
        #move values 3 times
                                  
        for x in range(3):
                for y in range(4):
                        if grid[x][y] == 0:
                                        grid[x][y] = grid[x+1][y]        
                                        grid[x+1][y] = 0    
                                
                                                                
        for x in range(3):
                for y in range(4):
                        if grid[x][y] == 0:
                                        grid[x][y] = grid[x+1][y]        
                                        grid[x+1][y] = 0                            
                                                                                        
        for x in range(3):
                for y in range(4):
                        if grid[x][y] == 0:
                                        grid[x][y] = grid[x+1][y]        
                                        grid[x+1][y] = 0


                        
        return grid

def push_down (grid):
        #0  [0,0,0,0],
        #1  [0,0,0,0],
        #2  [0,0,0,0],
        #3  [0,0,0,0]
        
        
        #move values 3 times
        for x in range(3,0,-1):
                for y in range(4):
                        if grid[x][y] == 0:
                                grid[x][y] = grid[x-1][y]        
                                grid[x-1][y] = 0 

        for x in range(3,0,-1):
                for y in range(4):
                        if grid[x][y] == 0:
                                grid[x][y] = grid[x-1][y]        
                                grid[x-1][y] = 0 
                                
        for x in range(3,0,-1):
                for y in range(4):
                        if grid[x][y] == 0:
                                grid[x][y] = grid[x-1][y]        
                                grid[x-1][y] = 0 
         
        #adds same numbers
        for x in range(3,0,-1):
                for y in range(4):
                        if grid[x-1][y] == grid[x][y]:
                                grid[x][y] = grid[x-1][y] + grid[x][y]        
                                grid[x-1][y] = 0 
        #move values 3 times                        
        for x in range(3,0,-1):
                for y in range(4):
                        if grid[x][y] == 0:
                                grid[x][y] = grid[x-1][y]        
                                grid[x-1][y] = 0 
                        
        for x in range(3,0,-1):
                for y in range(4):
                        if grid[x][y] == 0:
                                grid[x][y] = grid[x-1][y]        
                                grid[x-1][y] = 0 
                                                        
        for x in range(3,0,-1):
                for y in range(4):
                        if grid[x][y] == 0:
                                grid[x][y] = grid[x-1][y]        
                                grid[x-1][y] = 0 
        
                

                                

                                
                                                                          
        return grid
          
def push_right (grid):
        #    0 1 2 3     
        #0  [0,0,0,0],
        #1  [0,0,0,0],
        #2  [0,0,0,0],
        #3  [0,0,0,0]
        
        
  
                                
        #move values 3 times
        for y in range(3):
                for x in range(4):
                        if grid[x][y+1] == 0:
                                grid[x][y+1] = grid[x][y]        
                                grid[x][y] = 0    
        for y in range(3):
                for x in range(4):
                        if grid[x][y+1] == 0:
                                grid[x][y+1] = grid[x][y]        
                                grid[x][y] = 0    
          
        for y in range(3):
                for x in range(4):
                        if grid[x][y+1] == 0:
                                grid[x][y+1] = grid[x][y]        
                                grid[x][y] = 0 
                                
        #adds same numbers
        for y in range(3):
                for x in range(4):
                        if grid[x][y+1] == grid[x][y]:
                                grid[x][y+1] = grid[x][y] + grid[x][y+1]        
                                grid[x][y] = 0
                                
        #move values 3 times
        for y in range(3):
                for x in range(4):
                        if grid[x][y+1] == 0:
                                grid[x][y+1] = grid[x][y]        
                                grid[x][y] = 0    
        for y in range(3):
                for x in range(4):
                        if grid[x][y+1] == 0:
                                grid[x][y+1] = grid[x][y]        
                                grid[x][y] = 0    
                                  
        for y in range(3):
                for x in range(4):
                        if grid[x][y+1] == 0:
                                grid[x][y+1] = grid[x][y]        
                                grid[x][y] = 0 
                                
         
        return grid        
        
def push_left (grid):
        #    0 1 2 3     
        #0  [0,0,0,0],
        #1  [0,0,0,0],
        #2  [0,0,0,0],
        #3  [0,0,0,0]
        
        
        #move values 3 times
 

        for x in range(3):
                for y in range(4):
                        if grid[y][x] == 0:
                                grid[y][x] =grid[y][x+1]        
                                grid[y][x+1] = 0 
        for x in range(3):
                for y in range(4):
                        if grid[y][x] == 0:
                                grid[y][x] =grid[y][x+1]        
                                grid[y][x+1] = 0 
        for x in range(3):
                for y in range(4):
                        if grid[y][x] == 0:
                                grid[y][x] =grid[y][x+1]        
                                grid[y][x+1] = 0    
        #adds same numbers                       
        for x in range(3):
                for y in range(4):
                        if grid[y][x] == grid[y][x+1]:
                                grid[y][x] = grid[y][x] + grid[y][x+1]        
                                grid[y][x+1] = 0 
        #move values 3 times                       
        for x in range(3):
                for y in range(4):
                        if grid[y][x] == 0:
                                grid[y][x] =grid[y][x+1]        
                                grid[y][x+1] = 0 
        for x in range(3):
                for y in range(4):
                        if grid[y][x] == 0:
                                grid[y][x] =grid[y][x+1]        
                                grid[y][x+1] = 0 
        for x in range(3):
                for y in range(4):
                        if grid[y][x] == 0:
                                grid[y][x] =grid[y][x+1]        
                                grid[y][x+1] = 0
                               
        return grid              
                                

