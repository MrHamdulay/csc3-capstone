"""2048 a puzzle game
27/04/2013
Elizabeth Cilliers"""


import util

def push_up (grid):
    """merge grid values upwards"""
    
    #move all numbers upwards if they have an empty space above it.
    
#shift numbers up
    for shifts in range(4): #for the amount of times that the number can shift in the grid. 
        for row in range(4):
            for col in range(4):
                if grid[row][col] ==0: #check for empty spaces. if element is 0 then take the element below it and make it equal to the element above.
                    if (row+1)<=3: #the (row+1) number cant be more than 3. 
                        grid[row][col]= grid[row+1][col] 
                        grid[row+1][col]=0 #make the previous previous/original element equal to zero
 #merge equal adjacent numbers  
    for row in range(4):
            for col in range(4):    
                if (row+1)<=3: 
                    if grid[row][col]==grid[row+1][col]:
                        grid[row][col] += grid[row+1][col]
                        grid[row+1][col]=0
#check again for zeros and move numbers up                                       
    for row in range(4):
            for col in range(4):
                    if grid[row][col] ==0: 
                        if (row+1)<=3: 
                                grid[row][col]= grid[row+1][col] 
                                grid[row+1][col]=0                   
                    
def push_down (grid):
    """merge grid values downwards"""
    
    #move all numbers downwards if they have an empty space above it.
    #check for empty spaces.

    for shifts in range(4): #for the amount of times that the number can shift in the grid. 
        for row in range(4):
            for col in range(4):
                if grid[row][col] ==0: #check for empty spaces. if element is 0 then take the element above it and make it equal to the element below.
                    if (row-1)>=0: #the (row-1) number cant be less than zero. 
                        grid[row][col]= grid[row-1][col] 
                        grid[row-1][col]=0 #make the previous previous/original element equal to zero
    
    for row in range(4):
        for col in range(4):                    
                if (row-1)>=0:   
                    if grid[row][col]==grid[row-1][col]: 
                        grid[row][col] += grid[row-1][col] 
                        grid[row-1][col]=0
    
    for row in range(4):
        for col in range(4):
                if grid[row][col] ==0: 
                    if (row-1)>=0:  
                        grid[row][col]= grid[row-1][col] 
                        grid[row-1][col]=0    

def push_left (grid):
    """merge grid values left"""
    
    #move all numbers downwards if they have an empty space above it.
    #check for empty spaces.

    for shifts in range(4): #for the amount of times that the number can shift in the grid. 
        for row in range(4):
            for col in range(4):
                if grid[row][col] ==0: #check for empty spaces. if element is 0 then take the element on the right and make it equal to the element on the left.
                    if (col+1)<=3: #the (col+1) number cant be more than 3.
                        grid[row][col]= grid[row][col+1] 
                        grid[row][col+1]=0 #make the previous previous/original element equal to zero
   
    for row in range(4):
        for col in range(4):                         
                if (col+1)<=3: #if (col+1) less than 4, and if element on right and left is equal then add those values together. Then make value on right equal to zero. 
                    if grid[row][col]==grid[row][col+1]:
                        grid[row][col] += grid[row][col+1]
                        grid[row][col+1]=0
                  
    for row in range(4):
        for col in range(4):
                if grid[row][col] ==0: 
                    if (col+1)<=3: 
                        grid[row][col]= grid[row][col+1] 
                        grid[row][col+1]=0                        
                        
def push_right (grid):
    """merge grid values right""" 
    
    #move all numbers downwards if they have an empty space above it.
    #check for empty spaces.

    for shifts in range(4): #for the amount of times that the number can shift in the grid. 
        for row in range(4):
            for col in range(4):
                if grid[row][col] ==0: #check for empty spaces. if element is 0 then take the element on the left and make it equal to the element on the right.
                    if (col-1)>=0: #the (col-1) number cant be less than zero.
                        grid[row][col]= grid[row][col-1] 
                        grid[row][col-1]=0 #make the previous previous/original element equal to zero
    
    for row in range(4):
            for col in range(4):                    
                if (col-1)>=0: #if (col-1) is less than or equal to zero, and if element to right and left is equal then add those values together and push to right. 
                    if grid[row][col]==grid[row][col-1]:
                        grid[row][col] += grid[row][col-1]
                        grid[row][col-1]=0
    
    for row in range(4):
            for col in range(4):
                if grid[row][col] ==0: 
                    if (col-1)>=0: 
                        grid[row][col]= grid[row][col-1] 
                        grid[row][col-1]=0    