#Question 3
#Assignment 7
#Tauriq Dolley

#Define four functions that push values in a group in the respective direction

def push_right (grid):
    row = []
        
    for j in range(4):  
        row = grid[j]
        
        for i in range(0,3):        #removes all zeroes between things
            if row[i+1] == 0:
                row[i+1] = row[i]
                row[i] = 0              
            
            if row[i] == row[i+1]:
                row[i+1] = row[i] + row[i+1]
                row[i] = 0
                      
            
        for i in range(0,3):
            if row[i+1] == 0:
                row[i+1] = row[i]
                row[i] = 0
                
        for i in range(0,3):
            if row[i+1] == 0:
                row[i+1] = row[i]
                row[i] = 0
        
                
                           
    return grid
            
            
def push_left (grid):
    
    row = []
        
    for j in range(4):
        row = grid[j]
        
        for i in range(3,0,-1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
                
            if row[i-1] == row[i]:
                row[i] = row[i-1] + row[i]
                row[i-1] = 0
            
        for i in range(3,0,-1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
                
        for i in range(3,0,-1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
                
        for i in range(3,0,-1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0               
        
        
        

                
           
            
       # for i in range(len(row)-1,0,-1):
          #  if row[i-1] == 0:
          #      row[i-1] = row[i]
          #      row[i] = 0            
            
    return grid    
    