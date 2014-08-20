#kereshnee pillay
#2 may
#moving grid on 2048

#merge values up
def push_up (grid):
    for i in range (3):
        for j in range(3):
            for k in range(4):
#check if the above number is equal to 0
                if grid[j][k] == 0:
#if above number equals 0, set above number to equal bottom number
                    grid[j][k] = grid[j+1][k]
#set bottom number to equal 0
                    grid[j+1][k] = 0
    
    for i in range(3):
        for k  in range (4):
#check if above number equals bottom number
            if grid[i][k] == grid[i+1][k]:
#if equal, above number doubles
                grid[i][k] *= 2
#bottom number equals 0
                grid[i+1][k] = 0
         
#repeat pushing all numbers right to fill gaps that may have been caused by adding two numbers  
    for i in range (3):
        for j in range(3):
            for k in range(4):
                if grid[j][k] == 0:
                    grid[j][k] = grid[j+1][k]
                    grid[j+1][k] = 0                

#merge down
def push_down (grid):
    for i in range (3):
        for j in range(3):
            for k in range(4):
#check if the bottom number is equal to 0
                if (grid[j+1][k] == 0):
#if bottom number equals 0, set above number to equal above number
                    grid[j+1][k] = grid[j][k]
#set above number to equal 0
                    grid[j][k] = 0
                
    for i in range(3, 0, -1):
        for k  in range (4):
#check if bottom number equals above number
            if grid[i][k] == grid[i-1][k]:
#if equal, bottom number doubles
                grid[i][k] *= 2
#top number equals 0
                grid[i-1][k] = 0  
          
#repeat pushing all numbers right to fill gaps that may have been caused by adding two numbers       
    for t in range (3):
        for i in range(3):
            for k in range(4):
                if (grid[i+1][k] == 0):
                    grid[i+1][k] = grid[i][k]
                    grid[i][k] = 0
                
#merge values to the left
def push_left (grid):
    for t in range (3):
        for i in range(4):
            for j in range(3):
#check if the number to the left is equal to 0
                if grid[i][j] == 0:
#if number on left equals 0, set number on right to equal number on left
                    grid[i][j] = grid[i][j+1]
#set number on right to equal 0
                    grid[i][j+1] = 0
                    
    for i in range(4):
        for j in range (3):
#check if number on left equals number on right
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] *= 2
                grid[i][j+1] = 0
            
#repeat pushing all numbers right to fill gaps that may have been caused by adding two numbers     
    for t in range (3):
        for i in range(4):
            for j in range(3):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i][j+1]
                    grid[i][j+1] = 0    
    
  
#merge valuse to right
def push_right (grid):
    for k in range (4):
        for i in range(4):
            for j in range(3, 0, -1):
                 #check if the number to the right is equal to 0
                if grid[i][j] == 0: 
                    #if number on right equals 0, set number on right to equal number on left
                    grid[i][j] = grid[i][j-1] 
                    #set number on left to equal 0
                    grid[i][j-1] = 0
                    
    for i in range(4):
        for j in range (3):
            #check if number on right equals number on left
            if grid[i][j] == grid[i][j+1]:
                #if equal, number on right doubles
                grid[i][j] *= 2
                #number on left equals 0
                grid[i][j+1] = 0
                
    #repeat pushing all numbers right to fill gaps that may have been caused by adding two numbers 
    for t in range (4):
        for i in range(4):
            for j in range(3, 0, -1):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i][j-1]
                    grid[i][j-1] = 0  