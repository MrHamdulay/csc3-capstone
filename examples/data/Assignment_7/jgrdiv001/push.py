""""Assinment 7 question3
program to create push functions for game
author : Divan Jagers
27 April 2014"""

def push_up (grid):
    """merge grid values upwards"""
    #shifts each row to its maximum possible boundry
    z=0
    while z < 4:
        i=3
        while i > 0:
            j=0
            while j < 4:
                if grid[i-1][j]==0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0
                j+=1
            i+=-1
        z+=1
    #merges two values if they are found in the same column
    i=0
    while i < 3:
        j=0
        while j < 4:        
            if grid[i][j]==grid[i+1][j]:
                grid[i][j]=(grid[i][j])*2
                grid[i+1][j]=0
            j+=1
        i+=1
            
    #shifts the values up one more time to thier maximum possible boundries            
    z=0
    while z < 4:
        i=3
        while i > 0:
            j=0
            while j < 4:
                if grid[i-1][j]==0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0
                j+=1
            i+=-1
        z+=1
def push_down (grid):
    """merge grid values downwards"""
    z = 0
    while z < 4:     # iteration that shifts each row downward until at lowest row possible         
        i=2
        while i > -1:
            j=0
            while j < 4:
                if grid[i+1][j]==0:     #checks if the block is empty  
                    grid[i+1][j]=grid[i][j] #if it is empty, it will be replaced by one above it
                    grid[i][j]=0   # the block above becomes empty
                j+=1
            i+=-1
        z+=1     
    i=2
    while i >-1:    #checks to see if two values in the same column have the same value and then merges the two blocks
        j=0
        while j < 4:
            if grid[i][j]==grid[i+1][j]:   #checks if block is = block below it
                grid[i+1][j]=(grid[i+1][j])*2   #if so then double the block below
                grid[i][j]=0   #and make the top one zero
            j+=1
        i+=-1    
    z=0
    while z < 4:       #iteration that shifts the whole row down again until their maximum points
        i=2
        while i > -1:
            j=0
            while j < 4:
                if grid[i+1][j]==0:
                    grid[i+1][j]=grid[i][j]
                    grid[i][j]=0   
                j+=1
            i+=-1
        z+=1            
def push_left (grid):
    """merge grid values left"""
    z=0
    while z < 4:      #shifts the grid values to their most maximum left positions
        i=0
        for i in range(4): 
            j=3
            while j > 0: 
                if grid[i][j-1]==0:   #checks if the value to the most left is empty
                    grid[i][j-1]=grid[i][j]  #if empty, then make it equal to value right of it
                    grid[i][j]=0   #it then makes the value right of it empty
                j+=-1
            i+=1
        z+=1           
    i=0
    while i < 4:        #merges two values in the same row
        j=0
        while j < 3: 
            if grid[i][j]==grid[i][j+1]:  #checks to see if the values are the same
                grid[i][j]=(grid[i][j])*2 #if so then double the value to the left
                grid[i][j+1]=0    #and make the one to the right of it empty
            j+=1
        i+=1                            
    z=0
    while z < 4:   #repeats the whole shifting of values to the left
        i=0
        while i < 4: 
            j=3
            while j > 0: 
                if grid[i][j-1]==0:
                    grid[i][j-1]=grid[i][j]
                    grid[i][j]=0
                j+=-1
            i+=1
        z+=1  
def push_right (grid):
    """merge grid values right"""    
    z=0
    while z < 4:   #shifts the grid values to their most maximum right positions
        i=0
        while i < 4:
            j=0 
            while j < 3: 
                if grid[i][j+1]==0:   #checks if the value to the most right is empty
                    grid[i][j+1]=grid[i][j]  #if empty, then make it equal to value left of it
                    grid[i][j]=0   #make the value to the left of it then empty
                j+=1
            i+=1
        z+=1
    
    i=0
    while i < 4:   #merges two values in the same row
            j=3
            while j > 0: 
                if grid[i][j]==grid[i][j-1]:   #cheks if values are equal to each other and to the right
                    grid[i][j]=(grid[i][j])*2 #if so then double the value to the left
                    grid[i][j-1]=0  #and make the value right of it empty
                j+=-1
            i+=1
    z=0
    while z < 4:   # a repetition of the push right function algorithm as above
        i=0
        while i < 4:
            j=0
            while j < 3: 
                if grid[i][j+1]==0:
                    grid[i][j+1]=grid[i][j]
                    grid[i][j]=0    
                j+=1
            i+=1
        z+=1